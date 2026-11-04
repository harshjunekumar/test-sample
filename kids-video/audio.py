"""Narration (Kokoro TTS), original music and sound effects for "Count to 10 with Pip".
Writes build/audio.wav (exactly 60.000 s) and build/timeline.json (captions + lip-sync envelope)."""
import json, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

SR, DUR, FPS = 24000, 60.0, 30
N = int(SR * DUR)
VOICE, SPEED = "af_heart", 0.92
NUM = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]

# (start s, spoken text, on-screen caption)
LINES = [
    (0.35, "Hi friends! Look! A magic apple tree!", "Hi friends!"),
    (3.0, "How many apples can we count?", "How many apples?"),
    (5.6, "I'm Pip the Puppy! Let's count from one to ten!", "Let's count 1 to 10!"),
    (10.4, "Hold up your fingers, and count with me!", "Count with me!"),
]
QUIZ_T0, QUIZ_STEP = 40.9, 0.58
COUNT_T0, COUNT_STEP = 14.6, 1.9                     # numbers 1..10 at 14.6, 16.5 ... 31.7
LINES += [(COUNT_T0 + i * COUNT_STEP, NUM[i] + "!", None) for i in range(10)]
LINES += [
    (33.15, "Ten apples! Hooray!", "10 apples!"),
    (35.4, "Quiz time! How many stars do you see?", "How many stars?"),
    *[(QUIZ_T0 + i * QUIZ_STEP, NUM[i] + "!", None) for i in range(4)],
    (43.35, "Four stars! You got it!", "4 stars! You got it!"),
    (45.4, "Now let's count super fast!", "Count super fast!"),
]
FAST_T0, FAST_STEP = 47.5, 0.68                        # 47.5 ... 53.62
LINES += [(FAST_T0 + i * FAST_STEP, NUM[i] + "!", None) for i in range(10)]
LINES += [(55.2, "Hooray! You can count to ten! Great job!", "Great job!")]


def trim(x, thr=0.01):
    idx = np.where(np.abs(x) > thr)[0]
    return x[max(idx[0] - 240, 0): idx[-1] + 480] if len(idx) else x


def env_follow(x, attack=0.004, release=0.12):
    a, r = np.exp(-1 / (SR * attack)), np.exp(-1 / (SR * release))
    y = np.zeros_like(x); v = 0.0
    ax = np.abs(x)
    for i in range(0, len(x), 64):                      # block-wise for speed
        m = ax[i:i + 64].max()
        v = a * v + (1 - a) * m if m > v else r * v + (1 - r) * m
        y[i:i + 64] = v
    return y


# ------------------------------------------------------------------ narration
kok = Kokoro("voices/kokoro-v1.0.onnx", "voices/voices-v1.0.bin")
voice = np.zeros(N)
spans = []
for start, text, cap in LINES:
    s, sr = kok.create(text, voice=VOICE, speed=SPEED, lang="en-us")
    assert sr == SR
    s = trim(np.asarray(s, dtype=np.float64))
    s = s / (np.abs(s).max() + 1e-9) * 0.9
    i0 = int(start * SR)
    voice[i0:i0 + len(s)] += s[: N - i0]
    spans.append({"start": start, "end": round(start + len(s) / SR, 3), "text": text, "caption": cap})
for a, b in zip(spans, spans[1:]):
    if a["end"] > b["start"] - 0.05:
        print(f"WARNING overlap: '{a['text']}' ends {a['end']} > next starts {b['start']}")

# ------------------------------------------------------------------ music (original, synthesized)
t = np.arange(N) / SR
BPM = 112; BEAT = 60 / BPM; BAR = 4 * BEAT
midi = lambda m: 440 * 2 ** ((m - 69) / 12)
music = np.zeros(N)


def add(sig, at, gain=1.0, buf=None):
    buf = music if buf is None else buf
    i0 = int(at * SR)
    if i0 >= N: return
    seg = sig[: N - i0]
    buf[i0:i0 + len(seg)] += gain * seg


def pluck(f, dur=0.6, bright=1.0):
    tt = np.arange(int(dur * SR)) / SR
    s = sum((0.6 ** k) * bright ** k * np.sin(2 * np.pi * f * (k + 1) * tt) * np.exp(-tt * (5 + 3 * k)) for k in range(5))
    return s * np.minimum(1, tt / 0.003)


def bell(f, dur=1.2):
    tt = np.arange(int(dur * SR)) / SR
    s = np.sin(2 * np.pi * f * tt) * np.exp(-tt * 3) + 0.4 * np.sin(2 * np.pi * f * 2.76 * tt) * np.exp(-tt * 7) \
        + 0.2 * np.sin(2 * np.pi * f * 5.4 * tt) * np.exp(-tt * 12)
    return s * np.minimum(1, tt / 0.002)


def bass(f, dur=0.45):
    tt = np.arange(int(dur * SR)) / SR
    s = np.tanh(1.5 * np.sin(2 * np.pi * f * tt)) * np.exp(-tt * 4)
    return s * np.minimum(1, tt / 0.005)


rng = np.random.default_rng(7)
def noise(dur): return rng.standard_normal(int(dur * SR))


def shaker(dur=0.07):
    n = noise(dur); n = np.diff(n, prepend=0)        # high-passed
    return n * np.exp(-np.arange(len(n)) / SR * 60)


def kick():
    tt = np.arange(int(0.25 * SR)) / SR
    return np.sin(2 * np.pi * (50 + 90 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 14)


def woodblock(f=900):
    tt = np.arange(int(0.12 * SR)) / SR
    return np.sin(2 * np.pi * f * tt) * np.exp(-tt * 45)


CHORDS = [(60, 64, 67), (55, 59, 62), (57, 60, 64), (53, 57, 60)]   # C G Am F
MELODY = [(0, 72), (1, 76), (1.5, 79), (2, 76), (3, 74),              # beat offset, midi (per 2 bars)
          (4, 72), (5, 74), (5.5, 76), (6, 72)]
QUIZ_PAUSE = (38.4, 41.0)
bar_i = 0
tb = 0.0
while tb < DUR:
    ch = CHORDS[bar_i % 4]
    in_pause = QUIZ_PAUSE[0] - 0.2 <= tb < QUIZ_PAUSE[1]
    for b8 in range(8):                                 # eighth-note arpeggio strum
        at = tb + b8 * BEAT / 2
        if QUIZ_PAUSE[0] <= at < QUIZ_PAUSE[1]: continue
        note = ch[[0, 1, 2, 1, 0, 2, 1, 2][b8]] + (12 if b8 in (2, 5) else 0)
        add(pluck(midi(note)), at, 0.22)
        if b8 % 2 == 1: add(shaker(), at, 0.05)
    for b in (0, 2):
        at = tb + b * BEAT
        if not (QUIZ_PAUSE[0] <= at < QUIZ_PAUSE[1]):
            add(bass(midi(ch[0] - 24)), at, 0.35); add(kick(), at, 0.35)
    if bar_i % 2 == 0 and not in_pause and tb > 1:
        for off, m in MELODY:
            at = tb + off * BEAT
            if not (QUIZ_PAUSE[0] <= at < QUIZ_PAUSE[1]): add(bell(midi(m)), at, 0.10)
    bar_i += 1; tb += BAR
# quiz "thinking" tick-tock during the answer pause
for k, at in enumerate(np.arange(QUIZ_PAUSE[0], QUIZ_PAUSE[1], BEAT / 1)):
    add(woodblock(1100 if k % 2 == 0 else 800), at, 0.25)
# gentle fade in / out
music *= np.minimum(1, t / 0.6) * np.minimum(1, (DUR - t) / 1.2)

# ------------------------------------------------------------------ sound effects
sfx = np.zeros(N)


def pop(f0=500):
    tt = np.arange(int(0.12 * SR)) / SR
    return np.sin(2 * np.pi * (f0 + 900 * tt / 0.12) * tt) * np.exp(-tt * 30)


def whoosh(d=0.6, up=True):
    n = noise(d); k = np.arange(len(n)) / len(n)
    sm = np.convolve(n, np.ones(6) / 6, mode="same")  # soft lowpass
    e = np.sin(np.pi * k) ** 2
    return (n - sm) * e * (0.6 + 0.4 * (k if up else 1 - k))


def sparkle(start_m=84, n=6, step=0.06):
    out = np.zeros(int((n * step + 1.0) * SR))
    for i in range(n):
        b = bell(midi(start_m + [0, 4, 7, 12, 16, 19, 24, 28][i % 8]), 0.8)
        i0 = int(i * step * SR); out[i0:i0 + len(b)] += b
    return out


def tada():
    out = np.zeros(int(1.6 * SR))
    for i, m in enumerate([72, 76, 79, 84]):
        b = pluck(midi(m), 1.2, 1.1); i0 = int(i * 0.09 * SR); out[i0:i0 + len(b)] += b
    return out


add(sparkle(), 0.1, 0.25, sfx)                              # magic tree appears
add(pop(400), 0.25, 0.35, sfx)                              # Pip pops in
for at in (14.2, 34.9, 45.0, 54.9):
    add(whoosh(), at, 0.18, sfx)                            # scene transitions
for i in range(10):
    add(pop(500 + i * 40), COUNT_T0 + i * COUNT_STEP + 0.55, 0.30, sfx)   # apple lands in ten-frame
    add(bell(midi(72 + [0, 2, 4, 5, 7, 9, 11, 12, 14, 16][i])), COUNT_T0 + i * COUNT_STEP + 0.55, 0.12, sfx)
add(tada(), 33.0, 0.3, sfx)
for i in range(4):
    add(bell(midi(79 + i * 2)), QUIZ_T0 + i * QUIZ_STEP, 0.18, sfx)  # each star counted
add(tada(), 43.3, 0.3, sfx)
for i in range(10):
    add(pop(600 + i * 50), FAST_T0 + i * FAST_STEP, 0.22, sfx)
add(sparkle(72, 8, 0.07), 55.0, 0.3, sfx); add(tada(), 55.1, 0.35, sfx)

# ------------------------------------------------------------------ mix (music ducks under voice)
venv = env_follow(voice, 0.01, 0.35)
duck = 1 - 0.55 * np.clip(venv / 0.25, 0, 1)
mix = 0.95 * voice + 0.55 * music * duck + 0.8 * sfx
mix = np.tanh(mix * 1.1) / np.tanh(1.1)                 # gentle limiter
mix = mix / np.abs(mix).max() * 0.89
sf.write("build/audio.wav", mix.astype(np.float32), SR)

# lip-sync envelope per video frame
le = env_follow(voice, 0.004, 0.06)
frames = int(DUR * FPS)
mouth = [round(float(min(1.0, le[int(f / FPS * SR): int((f + 1) / FPS * SR)].mean() / 0.22)), 3) for f in range(frames)]
json.dump({"lines": spans, "mouth": mouth, "count_t0": COUNT_T0, "count_step": COUNT_STEP,
           "fast_t0": FAST_T0, "quiz_t0": QUIZ_T0, "quiz_step": QUIZ_STEP, "fast_step": FAST_STEP, "quiz_pause": QUIZ_PAUSE}, open("build/timeline.json", "w"))
for s in spans: print(f"{s['start']:6.2f}-{s['end']:6.2f}  {s['text']}")
print("audio seconds:", len(mix) / SR)
