# Business Requirements Document: Digital Loan Origination System (DLOS)

| Field | Value |
|---|---|
| Project | Digital Loan Origination System |
| Version | 1.2 (Approved) |
| Author | Business Analyst |
| Sponsor | Head of Retail Lending |
| Status | Signed off by Lending, Credit Risk, Compliance, IT |

---

## 1. Executive summary
FinServe Bank processes about **2,400 personal loan applications a month** through paper forms, email and manual underwriting. The process is slow (7–10 days), costly (~$145 per application) and error-prone. About 35% of applicants drop out, mostly to fintech competitors that decide within minutes.

DLOS will digitise the journey end to end: online application, automated document and identity checks, rules-based credit decisioning for standard cases, and a workflow for the underwriters who handle exceptions.

## 2. Business objectives
| ID | Objective | Measure | Target |
|---|---|---|---|
| BO-1 | Faster decisions | Median time application → decision | < 1 business day for 70% of applications |
| BO-2 | Reduce abandonment | % of started applications not submitted | < 15% (from ~35%) |
| BO-3 | Lower cost to serve | Fully-loaded cost per application | ~$55 (from ~$145) |
| BO-4 | Improve compliance | KYC/AML audit findings per year | < 3 (from 12) |
| BO-5 | Grow volume | Funded loans per month | +25% within 12 months |

## 3. Scope
**In scope**
- Unsecured personal loans ($1K–$50K) for new and existing retail customers
- Web and mobile-web application journey
- eKYC (ID document + selfie), credit bureau pull, income verification via open banking
- Rules-based auto-decision engine with manual underwriting queue
- e-Signature of loan agreement and handover to core banking for disbursement
- Operational dashboard for Lending Ops

**Out of scope**
- Mortgages, auto loans, business lending (phase 2)
- Native mobile apps
- Changes to the core banking system beyond the existing disbursement API

## 4. Stakeholders
See [stakeholders_raci.md](stakeholders_raci.md).

## 5. Current state (AS-IS) summary
See [process_maps.md](process_maps.md). Key pain points:
1. Paper forms are incomplete 40% of the time, which creates back-and-forth with the applicant
2. Data is re-keyed into 3 systems (CRM, credit scoring, core banking)
3. ID checks are manual and inconsistent, which drives audit findings
4. Every application goes to an underwriter, even low-risk ones
5. Applicants get no status visibility, so the call centre receives about 1,100 "where is my loan?" calls a month

## 6. Business requirements
| ID | Requirement | Priority | Objective |
|---|---|---|---|
| BR-01 | Applicants must be able to apply online 24/7 from any device | Must | BO-1, BO-2 |
| BR-02 | The bank must verify applicant identity digitally in line with KYC/AML policy | Must | BO-4 |
| BR-03 | Low-risk applications that meet policy must be decided automatically | Must | BO-1, BO-3 |
| BR-04 | Exceptions must route to underwriters with all information in one place | Must | BO-1, BO-3 |
| BR-05 | Applicants must be able to track application status | Should | BO-2 |
| BR-06 | Approved applicants must sign and receive funds without visiting a branch | Must | BO-1, BO-5 |
| BR-07 | Management must see real-time pipeline and SLA metrics | Should | BO-1, BO-3 |
| BR-08 | Every decision must be explainable and auditable | Must | BO-4 |

## 7. Functional requirements
| ID | Requirement | Parent BR | Priority |
|---|---|---|---|
| FR-01 | System shall provide a multi-step online application form with save-and-resume | BR-01 | Must |
| FR-02 | System shall pre-fill known data for existing customers after login | BR-01 | Should |
| FR-03 | System shall validate mandatory fields and formats in real time | BR-01 | Must |
| FR-04 | System shall capture a government ID and selfie and run liveness and match checks via the eKYC provider | BR-02 | Must |
| FR-05 | System shall screen applicants against sanctions and PEP lists | BR-02 | Must |
| FR-06 | System shall retrieve credit bureau report and score with applicant consent | BR-03 | Must |
| FR-07 | System shall verify income via open-banking connection or payslip upload | BR-03 | Must |
| FR-08 | Decision engine shall apply configurable credit policy rules and return Approve / Refer / Decline | BR-03 | Must |
| FR-09 | Credit Risk shall be able to change rule thresholds without a code release, subject to maker-checker approval | BR-03, BR-08 | Should |
| FR-10 | Referred applications shall enter an underwriter queue prioritised by SLA | BR-04 | Must |
| FR-11 | Underwriter workbench shall show application, documents, bureau data and rule outcomes on one screen | BR-04 | Must |
| FR-12 | Underwriters shall be able to request more documents from the applicant in-system | BR-04 | Should |
| FR-13 | System shall send status notifications (email/SMS) at each stage | BR-05 | Should |
| FR-14 | Applicant portal shall show current status and next steps | BR-05 | Could |
| FR-15 | System shall generate a loan agreement and collect e-signature | BR-06 | Must |
| FR-16 | System shall send approved, signed loans to core banking via disbursement API | BR-06 | Must |
| FR-17 | Dashboard shall show volumes, conversion funnel, auto-decision rate and SLA breaches | BR-07 | Should |
| FR-18 | System shall log every decision with inputs, rules fired, user and timestamp | BR-08 | Must |

## 8. Non-functional requirements
| ID | Category | Requirement |
|---|---|---|
| NFR-01 | Performance | Auto-decision returned within 60 seconds of submission (p95) |
| NFR-02 | Availability | 99.5% monthly uptime for applicant-facing services |
| NFR-03 | Security | Data encrypted in transit (TLS 1.2+) and at rest; role-based access |
| NFR-04 | Privacy | Compliant with applicable data-protection law; consent captured and stored |
| NFR-05 | Accessibility | Applicant journey meets WCAG 2.1 AA |
| NFR-06 | Audit | Decision logs retained for 7 years and cannot be modified |
| NFR-07 | Scalability | Supports 3× current volume without degradation |

## 9. Assumptions, constraints & dependencies
- **Assumption:** the existing core banking disbursement API can be reused without change
- **Assumption:** eKYC and open-banking vendors are already approved by Procurement
- **Constraint:** go-live before the Q2 peak lending season; fixed budget
- **Dependency:** Credit Risk to deliver documented policy rules by Sprint 3

## 10. Risks
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Credit policy rules not finalised in time | Medium | High | Weekly rules workshop; start with conservative rule set |
| Auto-decisioning introduces bias | Low | High | Fairness testing on historical data; Compliance review of rules |
| Low adoption by underwriters | Medium | Medium | Involve underwriters in workbench design; training & champions |
| Vendor API outages | Medium | Medium | Graceful fallback to manual review queue |

## 11. Success criteria & sign-off
DLOS is successful when objectives BO-1 to BO-4 are met for 3 consecutive months after go-live.

| Role | Name | Decision | Date |
|---|---|---|---|
| Head of Retail Lending (Sponsor) | — | Approved | — |
| Chief Credit Officer | — | Approved | — |
| Head of Compliance | — | Approved | — |
| IT Delivery Lead | — | Approved | — |
