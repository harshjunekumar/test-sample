# Count to 10 with Pip: 60-second kids' learning Short

`output/Count-to-10-with-Pip.mp4` is 60.000 s, 1080 × 1920 (9:16), 30 fps, H.264 + AAC, loudness -14.8 LUFS.
It's ready for YouTube Shorts and Instagram Reels.

**Topic:** counting 1 to 10, ages 2–7. The guide is **Pip the Puppy**, the same character as on the *Color Me Happy!* coloring book cover.

| Time | What happens | Learning technique |
|---|---|---|
| 0–5 s | Pip says hi; a magic apple tree grows. "How many apples can we count?" | Hook question |
| 5–15 s | Pip introduces the goal; a ten-frame (2 × 5 boxes) appears. "Hold up your fingers and count with me!" | Count-along |
| 15–35 s | Each apple flies from the tree into the ten-frame as Pip says the number. A big number badge and the number word show for each one. | Visual association (1 apple = 1 box), counting objects one at a time |
| 35–45 s | Quiz: "How many stars do you see?" A 3.5-second pause with tick-tock music lets kids answer. Then the stars are counted 1–4: "Four stars! You got it!" | Active recall, pause to answer, praise |
| 45–55 s | "Let's count super fast!" Balloons 1–10 pop in as Pip counts. | Repetition |
| 55–60 s | Confetti: "Hooray! You can count to ten! Great job!" | Positive reinforcement, takeaway |

## Files
- `audio.py`: narration script and timing, plus the original synthesized music (C–G–Am–F, 112 BPM) and sound effects, with the music ducking under the voice.
- `scene.html`: the animation, drawn on a canvas one frame at a time.
- `render.js`: turns those frames into the MP4 through FFmpeg, and also saves single preview stills.
- `build.sh`: rebuilds everything with one command.

## Voice and licenses
The voice is [Kokoro-82M](https://github.com/thewh1teagle/kokoro-onnx) (Apache-2.0, free for commercial use), voice `af_heart`.
To rebuild, download `kokoro-v1.0.onnx` and `voices-v1.0.bin` into `voices/`. They aren't committed because they're 350 MB.
The music and sound effects are synthesized from scratch in `audio.py`, and the font is Fredoka (SIL OFL), so you have no third-party music or art licensing issues.
