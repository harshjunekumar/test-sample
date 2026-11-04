#!/usr/bin/env bash
# Rebuild "Count to 10 with Pip" (60 s, 1080x1920). Needs: python3, node + playwright, ffmpeg,
# pip install kokoro-onnx soundfile numpy, and the Kokoro model files in voices/ (see README.md).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p build output
python3 audio.py                                   # narration + music + SFX -> build/audio.wav, build/timeline.json
node render.js video                               # frames -> output/Count-to-10-with-Pip.mp4
# loudness-normalise to -14 LUFS (YouTube/Instagram) and remux
J=$(ffmpeg -hide_banner -i build/audio.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/^{/,/^}/p')
MI=$(echo "$J" | python3 -c "import json,sys;d=json.load(sys.stdin);print(f\"measured_I={d['input_i']}:measured_TP={d['input_tp']}:measured_LRA={d['input_lra']}:measured_thresh={d['input_thresh']}:offset={d['target_offset']}\")")
ffmpeg -y -loglevel error -i build/audio.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11:$MI:linear=true" -ar 48000 build/audio_norm.wav
ffmpeg -y -loglevel error -i output/Count-to-10-with-Pip.mp4 -i build/audio_norm.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -t 60 -movflags +faststart output/tmp.mp4
mv output/tmp.mp4 output/Count-to-10-with-Pip.mp4
node render.js preview 25.2 && cp build/preview_25.2.png output/thumbnail-cover-frame.png
echo "done: output/Count-to-10-with-Pip.mp4"
