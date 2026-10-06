# 📊 Juhi Bhalla | Business Analyst Portfolio

**E-commerce & Retail Business Analyst** · 5+ years across Flipkart (category growth) and Enverus (B2B SaaS commercial intelligence) · Bengaluru, India
🔗 [LinkedIn](https://www.linkedin.com/in/YOUR-LINKEDIN-ID) · ✉️ juhibhalla.jblko@gmail.com


Five end-to-end projects covering the full range of business analysis work: **data analysis**, **predictive insight with a business case**, **requirements engineering**, **AI-powered self-serve insights**, and a **customer-facing styling chatbot**. Each project starts from a business question and ends with clear recommendations.

| # | Project | Business question | Key skills | Headline result |
|---|---|---|---|---|
| 1 | [E-commerce Sales Performance & Customer Value](01-ecommerce-sales-analysis/) | *Where does our revenue come from, and are promotions paying off?* | SQL (CTEs, window functions), Python, KPI design, RFM, cohort retention | Found that 21–30% discounts cut margin from **40% → 13%**, and flagged a lapsing high-value segment worth **$1.09M in lifetime revenue** |
| 2 | [Customer Churn Analysis & Retention Business Case](02-customer-churn-analysis/) | *Why do customers leave, who's next, and is a retention campaign worth it?* | Root-cause analysis, logistic regression (AUC 0.81), risk scoring, ROI modelling | Showed a **targeted** campaign returns **+89% ROI**, while a blanket campaign **loses 47%** |
| 3 | [Digital Loan Origination: Requirements & Process Redesign](03-loan-origination-requirements/) | *How do we cut loan decisions from 10 days to same-day?* | BRD, AS-IS/TO-BE BPMN, gap analysis, user stories + Gherkin, RACI, RTM, UAT | Full requirements set: 8 business reqs → 18 functional reqs → 18 user stories → 26 traced test cases |
| 4 | [Persona Insights Chatbot](04-persona-insights-chatbot/) | *Can business teams get persona insights without waiting for an analyst?* | K-Means segmentation, persona design, LLM tool use (Claude API), Python | 5 behavioural personas behind a chatbot that answers only from calculated numbers. Includes a **free web chat app** (no API key) |
| 5 | [Just for you: Personal Styling Chatbot](05-just-for-you-stylist/) | *How do we help shoppers find outfits that suit them, and convert?* | Persona design, conversational UX, recommendation rules, trend research, Streamlit | 4 questions → style persona with colour-matched outfits, accessories and Google Shopping links. Free, public web app |

## 🧰 Toolkit
`SQL` · `Python (pandas, scikit-learn, matplotlib)` · `Claude API (tool use)` · `Excel / Power BI-ready CSV outputs` · `BPMN / Mermaid process modelling` · `Agile (Scrum, user stories, MoSCoW)` · `Requirements traceability` · `UAT`

## ▶️ Run the analytics projects
```bash
pip install -r requirements.txt
cd 01-ecommerce-sales-analysis && python generate_data.py && python analysis.py && cd ..
cd 02-customer-churn-analysis  && python generate_data.py && python analysis.py && cd ..
cd 04-persona-insights-chatbot  && python build_personas.py && streamlit run app.py   # free web chatbot
cd 05-just-for-you-stylist     && streamlit run app.py                               # styling chatbot
```
All datasets are synthetic and generated from a fixed seed, so every number in the READMEs can be reproduced exactly.

## 📣 Sharing on LinkedIn
See **[LINKEDIN_KIT.md](LINKEDIN_KIT.md)** for ready-to-post write-ups, Featured-section text and resume bullets.
