// Render SVG pages with Chromium: 300 DPI PNGs (2550x3300) + vector PDFs (US Letter and A4).
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const [svgDir, outDir, ...names] = process.argv.slice(2);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 850, height: 1100 }, deviceScaleFactor: 3 });
  for (const n of names) {
    const svg = fs.readFileSync(path.join(svgDir, n), 'utf8');
    await page.setContent(`<html><body style="margin:0;background:#fff">${svg.replace('width="8.5in" height="11in"', 'width="850" height="1100"')}</body></html>`);
    await page.screenshot({ path: path.join(outDir, 'png-300dpi', n.replace('.svg', '.png')), clip: { x: 0, y: 0, width: 850, height: 1100 } });
    console.log('png', n);
  }
  if (process.env.SKIP_PDF) { await browser.close(); return; }
  const all = fs.readdirSync(svgDir).filter(f => f.endsWith('.svg')).sort();
  for (const [fmt, w, h] of [['Letter', '8.5in', '11in'], ['A4', '210mm', '297mm']]) {
    const body = all.map(f => `<div class="pg">${fs.readFileSync(path.join(svgDir, f), 'utf8')
      .replace('width="8.5in" height="11in"', `width="${w}" height="${h}" preserveAspectRatio="xMidYMid meet"`)}</div>`).join('\n');
    await page.setContent(`<html><head><style>@page{size:${fmt};margin:0}html,body{margin:0;background:#fff}
      .pg{width:${w};height:${h};overflow:hidden;page-break-after:always;break-after:page}
      .pg:last-child{page-break-after:auto;break-after:auto} svg{display:block}</style></head><body>${body}</body></html>`);
    const file = path.join(outDir, `Fun-Adventures-and-Cute-Animals-Coloring-Book-${fmt}.pdf`);
    await page.pdf({ path: file, format: fmt, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    console.log('pdf', file, all.length, 'pages');
  }
  await browser.close();
})();
