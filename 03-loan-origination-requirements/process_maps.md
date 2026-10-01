# Process Maps: AS-IS vs TO-BE

> Diagrams use Mermaid, which GitHub renders automatically.

## AS-IS: paper-based loan process (7–10 business days)

```mermaid
flowchart LR
    subgraph Applicant
        A1([Needs loan]) --> A2[Collects paper form<br/>at branch / email]
        A2 --> A3[Fills form & gathers<br/>payslips, ID copies]
        A3 --> A4[Submits at branch]
        A9[Calls to chase status]
        A12[Visits branch to sign]
    end
    subgraph Branch Staff
        B1[Checks completeness] --> B2{Complete?}
        B2 -- No --> B3[Calls applicant<br/>for missing items]
        B3 --> A3
        B2 -- Yes --> B4[Photocopies ID<br/>manual KYC check]
        B4 --> B5[Re-keys data into CRM]
    end
    subgraph Lending Ops
        C1[Re-keys into<br/>credit scoring tool] --> C2[Pulls bureau report]
        C2 --> C3[Puts file in<br/>underwriter queue]
    end
    subgraph Underwriter
        D1[Reviews EVERY<br/>application manually] --> D2{Decision}
        D2 -- Need info --> B3
    end
    subgraph Ops & Core Banking
        E1[Prepares paper<br/>agreement] --> E2[Re-keys loan into<br/>core banking] --> E3([Disburse])
    end
    A4 --> B1
    B5 --> C1
    C3 --> D1
    D2 -- Approve --> E1
    E1 --> A12 --> E2
    D2 -- Decline --> A10([Decline letter posted])
    C3 -.-> A9
```

### Pain points identified
| # | Pain point | Root cause | Impact |
|---|---|---|---|
| P1 | 40% of forms incomplete | No validation, unclear guidance | 2–3 days of rework |
| P2 | Data re-keyed 3× | No integration between CRM, scoring, core | Errors, ~25 min per app |
| P3 | Manual ID checks | No eKYC tool | Inconsistent; 12 audit findings / yr |
| P4 | 100% of apps reviewed by an underwriter | No automated decisioning | Queue backlog, 4–5 day wait |
| P5 | No status visibility | No applicant notifications | ~1,100 chase calls / month |
| P6 | Branch visit required to apply and sign | Paper-only process | Drop-off; excludes remote customers |
| P7 | Underwriters gather data from 4 systems | No single view | ~30 min per review |
| P8 | Decisions poorly documented | Free-text notes | Hard to audit or explain decisions |
| P9 | No management reporting | Data spread across spreadsheets | SLA breaches found too late |

## TO-BE: digital loan origination (same day for ~70%)

```mermaid
flowchart LR
    subgraph Applicant
        A1([Needs loan]) --> A2[Applies online<br/>web / mobile]
        A2 --> A3[eKYC: ID + selfie]
        A3 --> A4[Consents to bureau &<br/>open-banking income check]
        A8[Receives status<br/>notifications]
        A9[e-Signs agreement]
    end
    subgraph DLOS Platform
        S1[Real-time validation<br/>& save-and-resume] --> S2[Sanctions / PEP screen]
        S2 --> S3[Bureau pull +<br/>income verification]
        S3 --> S4{Decision engine<br/>policy rules}
        S5[Generate agreement]
        S6[Audit log of every<br/>decision & rule fired]
    end
    subgraph Underwriter
        U1[Workbench: single view<br/>SLA-prioritised queue] --> U2{Decision}
        U2 -- Need info --> U3[Request docs in-system] --> A8
    end
    subgraph Core Banking
        C1[Disbursement API] --> C2([Funds released])
    end
    A2 --> S1
    A4 --> S2
    S4 -- Approve ~70% --> S5
    S4 -- Refer ~20% --> U1
    S4 -- Decline ~10% --> A8
    U2 -- Approve --> S5
    U2 -- Decline --> A8
    S5 --> A9 --> C1
    S4 -.-> S6
    U2 -.-> S6
```

## Gap analysis
| Area | AS-IS | TO-BE | Gap / change required | Requirement |
|---|---|---|---|---|
| Application capture | Paper form at branch | Online, validated, save-and-resume | Build digital form | FR-01–03 |
| Identity verification | Photocopy + visual check | eKYC with liveness + sanctions/PEP | Integrate eKYC vendor | FR-04, FR-05 |
| Income verification | Payslip copies | Open banking or upload | Integrate open-banking API | FR-07 |
| Credit decision | 100% manual | Rules engine; manual for exceptions only | Configure policy rules; maker-checker | FR-08, FR-09 |
| Underwriting | 4 systems, paper file | Single-view workbench | Build workbench & queue | FR-10–12 |
| Communication | Applicant calls to chase | Proactive email/SMS + portal | Notification service | FR-13, FR-14 |
| Contracting | Branch visit to sign | e-Signature | e-Sign integration | FR-15 |
| Disbursement | Re-keyed into core | API handover | Integrate existing API | FR-16 |
| Reporting | Manual spreadsheets | Real-time dashboard | Build ops dashboard | FR-17 |
| Audit | Free-text notes | Immutable decision log | Audit logging | FR-18 |

## Expected time saving per application
| Step | AS-IS | TO-BE |
|---|---:|---:|
| Capture & completeness checks | 2–3 days | Minutes (applicant self-serve) |
| Data entry (3×) | ~25 min staff time | 0 |
| KYC | ~1 day | < 2 min |
| Underwriting | 4–5 days queue | Instant (auto) / < 1 day (referred) |
| Contract & disbursement | 1–2 days + branch visit | Same day |
