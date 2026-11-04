// node render.js <html> <pdf> <widthIn> <heightIn> [png]
const { chromium } = require('playwright');
const path = require('path');
const [html, pdf, w, h, png] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: Math.round(w * 96), height: Math.round(h * 96) }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.resolve(html));
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: pdf, width: w + 'in', height: h + 'in', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  if (png) await p.screenshot({ path: png, fullPage: true });
  await b.close();
  console.log('wrote', pdf);
})();
