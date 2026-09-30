const { Document, Packer, Paragraph, TextRun, ExternalHyperlink, AlignmentType, BorderStyle } = require('docx');
const fs = require('fs');

const GREY = '6B6B6B', RULE = 'B7B7B7', LINK = '0563C1';

// parse **bold** markers into TextRuns
function runs(text, size = 19, color) {
  return text.split('**').map((p, i) => new TextRun({ text: p, bold: i % 2 === 1, size, color }));
}
function header(t) {
  return new Paragraph({ spacing: { before: 170, after: 55 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 2 } },
    children: [new TextRun({ text: t, bold: true, size: 22 })] });
}
function bullet(t) { return new Paragraph({ bullet: { level: 0 }, spacing: { after: 35 }, children: runs(t, 19) }); }
function jobline(company, rest, dates, companyBold = true) {
  return new Paragraph({ spacing: { before: 90, after: 18 }, children: [
    new TextRun({ text: company, bold: companyBold, size: 20 }),
    new TextRun({ text: rest ? ` - ${rest}  |  ` : `  |  `, size: 20 }),
    new TextRun({ text: dates, size: 20, color: GREY }),
  ]});
}
function plain(t, size = 19) { return new Paragraph({ spacing: { after: 30 }, children: runs(t, size) }); }

const SUMMARY = "E-commerce and retail Business Analyst with 5+ years owning category growth and analytics at Flipkart and Enverus (B2B SaaS). Expert in category strategy, assortment, pricing and promotions, demand forecasting, and 360° reporting - turning data into revenue and margin growth. Known for solving ambiguous problems through analytics and cross-functional stakeholder management.";
const FLIPKART_INTRO = "**Owned category, seller & SKU performance for a large marketplace category - driving growth via assortment, pricing, promotions, and demand planning across GMV, conversion, and in-stock.**";
const FLIPKART_BULLETS = [
  "Owned **cohort and SKU trend analysis** (YoY & MoM); used these insights to drive **product exchange bump-ups** on select high-value SKUs, growing overall category **revenue by 19% YoY**.",
  "Led **market research and assortment / selection analysis**; introduced the **Windows segment** into the assortment, lifting overall **Flipkart market-penetration share by ~1%**.",
  "Ran **cohort analysis, customer funnel metrics, and user personas**; launched **coupons for Flipkart loyal customers**, capturing category customers and driving a **20% improvement in conversion**.",
  "Analyzed **payment methods and bank cross-demographic behavior**; rolled out **South-specific bank coupons**, improving overall **bank-offer adoption and conversion across the South region**.",
  "Built and automated **Tableau / Power BI dashboards** (SQL, Google Apps Script) with standardized KPIs, giving leaders real-time visibility into category health.",
  "Built regression-based **demand and sales forecasting** to guide category planning; data-driven planning drove a **55% category revenue uplift during Big Billion Days**.",
];
const ENVERUS_BULLETS = [
  "Built and maintained **Tableau / Power BI dashboards** giving US commercial leaders real-time visibility into sales trends and KPIs, supporting **ARR that scaled into the $500MM range**.",
  "Re-engineered reporting through **Lean Six Sigma** optimization, driving a **20% reduction in cycle times** and standardizing KPIs across global teams.",
];
const ASSOCIATE_BULLET = "Published quantitative research across **3 cycles** and built financial / operational and unit-economics models; produced competitive and price intelligence to support leadership decisions.";
const CERTS = [
  "**Agile Project Management** - Google",
  "**Mastering Advanced SQL Queries** - Coursera",
  "**From Excel to Power BI** - Knowledge Accelerators",
  "**Customer Value, Acquisition, and Retention** - University of Maryland, College Park",
  "**Introduction to Generative AI** - Google Cloud",
  "**Generative AI for Leaders** - Vanderbilt University",
];
const LEADERSHIP = [
  "Led operations, logistics & teams for corporate / college events hosting **800-1,000+ participants**.",
  "Consistent data-led growth record - **55% BBD category uplift**, **19% YoY revenue growth**, and **20% faster reporting**.",
];

function buildChildren(opts) {
  const c = [];
  c.push(new Paragraph({ spacing: { after: 18 }, children: [new TextRun({ text: 'JUHI BHALLA', bold: true, size: 32 })] }));
  c.push(new Paragraph({ spacing: { after: 18 }, children: [
    new TextRun({ text: '+91 88709 52224   |   juhibhalla.jblko@gmail.com   |   ', size: 19 }),
    new ExternalHyperlink({ link: 'https://www.linkedin.com/in/juhi-bhalla', children: [new TextRun({ text: 'LinkedIn', size: 19, color: LINK, underline: {} })] }),
    new TextRun({ text: '   |   Bengaluru, India', size: 19 }),
  ]}));
  c.push(new Paragraph({ spacing: { after: 20 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: RULE, space: 4 } },
    children: [new TextRun({ text: 'Business Analyst | E-commerce & Retail | Category Growth | Assortment, Pricing & Promotions | Demand Planning | Data Analytics', size: 18, color: GREY })] }));

  c.push(header('PROFESSIONAL SUMMARY'));
  c.push(new Paragraph({ spacing: { after: 30 }, alignment: AlignmentType.JUSTIFIED, children: runs(SUMMARY, 19) }));

  c.push(header('EXPERIENCE'));
  c.push(jobline('Flipkart', opts.flipkartTitle, 'Jun 2024 - Sep 2026'));
  c.push(new Paragraph({ spacing: { after: 30 }, children: runs(FLIPKART_INTRO, 19) }));
  FLIPKART_BULLETS.forEach(b => c.push(bullet(b)));
  c.push(jobline('Enverus', 'Business Analyst I - Market Research (B2B SaaS)', 'Jan 2023 - May 2024'));
  ENVERUS_BULLETS.forEach(b => c.push(bullet(b)));
  c.push(jobline('Associate - Commercial Intelligence', '', 'May 2021 - Dec 2022'));
  c.push(bullet(ASSOCIATE_BULLET));

  c.push(header('EDUCATION'));
  c.push(new Paragraph({ spacing: { after: 16 }, children: [
    new TextRun({ text: 'B.Tech - Biotechnology', bold: true, size: 19 }),
    new TextRun({ text: ' | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10', size: 19 }),
  ]}));
  c.push(new Paragraph({ spacing: { after: 16 }, children: runs('**12th (ISC)** | Spring Dale College | 2016 | 88%     •     **10th (ICSE)** | Spring Dale College | 2014 | 88%', 19) }));

  c.push(header('SKILLS'));
  c.push(new Paragraph({ spacing: { after: 20 }, children: [new TextRun({ text: opts.skills, size: 19 })] }));

  if (opts.certs) {
    c.push(header('CERTIFICATIONS'));
    CERTS.forEach(b => c.push(bullet(b)));
  }

  c.push(header('LEADERSHIP & ACHIEVEMENTS'));
  LEADERSHIP.forEach(b => c.push(bullet(b)));
  return c;
}

const SKILLS_9 = "Category Growth | Category Management | Assortment & Merchandising | Pricing & Promotions | Demand Forecasting | Cohort & Conversion Analysis | Competitive Intelligence | Requirements (BRD / FRD) | Agile / Scrum | Stakeholder Management | Dashboards & 360° Reporting | SQL | Tableau | Power BI | Advanced Excel | Jira | Confluence | Python (familiarity)";
const SKILLS_6 = "Category Growth | Category Management | Assortment & Merchandising | Pricing & Promotions | Demand Forecasting | Cohort & Conversion Analysis | Competitive Intelligence | Dashboards & 360° Reporting | Stakeholder Management | SQL | Tableau | Power BI | Advanced Excel | Python (familiarity)";

const configs = [
  { file: '/home/user/test-sample/Juhi_Bhalla_Resume_9.docx',
    flipkartTitle: 'Business Analyst - Large Appliances (eCommerce Marketplace)', skills: SKILLS_9, certs: true },
  { file: '/home/user/test-sample/Juhi_Bhalla_Resume_6.docx',
    flipkartTitle: 'Assistant Manager - Business Development, Large Appliances (eCommerce)', skills: SKILLS_6, certs: false },
];

(async () => {
  for (const cfg of configs) {
    const doc = new Document({
      styles: { default: { document: { run: { font: 'Calibri', size: 19 } } } },
      sections: [{ properties: { page: { margin: { top: 600, bottom: 500, left: 720, right: 720 } } },
        children: buildChildren(cfg) }],
    });
    const buf = await Packer.toBuffer(doc);
    fs.writeFileSync(cfg.file, buf);
    console.log('wrote', cfg.file);
  }
})();
