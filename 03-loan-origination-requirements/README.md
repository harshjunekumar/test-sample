# 🏦 Digital Loan Origination: Requirements & Process Redesign

**Skills shown:** Requirements elicitation · BRD writing · AS-IS / TO-BE process mapping (BPMN-style) · Gap analysis · User stories with Gherkin acceptance criteria · MoSCoW prioritisation · Stakeholder analysis & RACI · Requirements Traceability Matrix · UAT planning

> **Scenario.** *FinServe Bank* (fictional) handles personal loan applications on paper and email. A decision takes **7–10 business days**, **~35% of applicants drop out**, and every application is re-keyed manually 3 times.
> As Business Analyst, I led discovery and defined requirements for a **digital loan origination system** with a target of **same-day decisions for 70% of applications**.

## 📁 Deliverables

| # | Document | What it shows |
|---|---|---|
| 1 | [Business Requirements Document](BRD.md) | Scope, objectives, business & functional requirements, NFRs, assumptions, risks |
| 2 | [Process Maps: AS-IS vs TO-BE](process_maps.md) | Swimlane flows (Mermaid), pain points, gap analysis |
| 3 | [User Stories & Acceptance Criteria](user_stories.md) | Epics, INVEST user stories, Gherkin scenarios, MoSCoW |
| 4 | [Stakeholder Analysis & RACI](stakeholders_raci.md) | Power/interest grid, engagement plan, RACI matrix |
| 5 | [Requirements Traceability Matrix](traceability_matrix.csv) | Business need → requirement → story → test case |
| 6 | [UAT Test Plan](uat_test_plan.md) | Entry/exit criteria, test cases, defect triage |

## 🎯 Outcomes (target KPIs)

| KPI | AS-IS | TO-BE target |
|---|---:|---:|
| Time to decision | 7–10 days | **< 1 day for 70% of apps** |
| Applicant drop-off | ~35% | **< 15%** |
| Manual re-keying per app | 3× | **0×** |
| Cost per application | ~$145 | **~$55** |
| Compliance audit findings | 12 / yr | **< 3 / yr** |

## 🧭 Approach

1. **Discovery**: 14 stakeholder interviews, 2 process walkthroughs at branches, and an analysis of 6 months of application data
2. **Analysis**: mapped the AS-IS process, found 9 pain points, and traced them to root causes (fishbone / 5 Whys)
3. **Definition**: wrote the BRD, then broke it into 5 epics and 18 user stories, prioritised with MoSCoW
4. **Validation**: requirement walkthroughs with Credit Risk, Compliance and IT, then sign-off
5. **Delivery support**: backlog refinement, traceability matrix, UAT plan and defect triage
