// node render.js preview 3 12 20 ...   -> build/preview_<t>.png
// node render.js video                 -> build/frames piped into ffmpeg -> output video with audio
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { spawn } = require('child_process');
const [mode, ...times] = process.argv.slice(2);
const FPS = 30, DUR = 60, FRAMES = FPS * DUR;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 540, height: 960 } });
  p.on('pageerror', e => { console.error('PAGE ERROR', e); process.exit(1); });
  await p.goto('file://' + path.resolve('scene.html'));
  await p.evaluate(tl => window.setTimeline(tl), JSON.parse(fs.readFileSync('build/timeline.json', 'utf8')));
  await p.evaluate(async () => { await document.fonts.load('700 50px Fredoka'); await document.fonts.load('500 50px Fredoka'); });
  const grab = async (t, q) => {
    const url = await p.evaluate(([t, q]) => { window.render(t); return document.getElementById('c').toDataURL(q ? 'image/jpeg' : 'image/png', q || undefined); }, [t, q]);
    return Buffer.from(url.split(',')[1], 'base64');
  };
  if (mode === 'preview') {
    for (const t of times) fs.writeFileSync(`build/preview_${t}.png`, await grab(parseFloat(t)));
  } else {
    fs.mkdirSync('output', { recursive: true });
    const out = 'output/Count-to-10-with-Pip.mp4';
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
      '-i', 'build/audio.wav', '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p',
      '-r', String(FPS), '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-t', String(DUR), '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let f = 0; f < FRAMES; f++) {
      const buf = await grab(f / FPS, 0.95);
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (f % 300 === 0) console.log('frame', f);
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
    console.log('wrote', out);
  }
  await b.close();
})();
