# UAT Test Plan: Digital Loan Origination System

## 1. Objective
Confirm that DLOS meets the approved business requirements ([BRD](BRD.md)) and is fit for use by applicants, underwriters, Lending Ops and Compliance before go-live.

## 2. Scope
- **In scope:** all Must and Should user stories (US-01 to US-18 except US-15), the end-to-end journey, and the integrations (eKYC, bureau, open banking, e-sign, core banking).
- **Out of scope:** performance/load testing (owned by IT), penetration testing (owned by InfoSec).

## 3. Entry & exit criteria
| Entry criteria | Exit criteria |
|---|---|
| SIT completed with no open Critical/High defects | 100% of Must test cases executed; ≥ 95% passed |
| UAT environment loaded with masked test data | 0 open Critical, ≤ 2 open High defects (with workaround and agreed fix date) |
| Test cases reviewed and signed off by business leads | Compliance sign-off on KYC & audit test cases |
| Testers trained on the system | Business sign-off from Sponsor and Lending Ops |

## 4. Test approach
- **Scenario-based end-to-end tests** using 6 test personas (prime borrower, thin-file borrower, borderline score, sanctions hit, expired ID, self-employed income)
- **Business-rule boundary tests** for the decision engine (scores 619/620/719/720; DTI 35%/36%; amount $25,000/$25,001)
- **Negative tests** for validation, expiry and lockout
- **Traceability:** every test case maps to a requirement in the [traceability matrix](traceability_matrix.csv)

## 5. Schedule
| Phase | Duration |
|---|---|
| UAT preparation (data, scripts, training) | 1 week |
| Cycle 1: execute all test cases | 1 week |
| Defect fix & retest | 1 week |
| Cycle 2: regression + sign-off | 3 days |

## 6. Defect severity & triage
| Severity | Definition | Target fix |
|---|---|---|
| Critical | Blocks the journey or causes a regulatory breach; no workaround | 24 hours |
| High | Major function wrong; workaround exists | 3 days |
| Medium | Minor function wrong; low business impact | Next release |
| Low | Cosmetic | Backlog |

Triage meets **daily** during UAT: the BA (chair), the Lending Ops test lead, the IT lead and Compliance when needed.

## 7. Status snapshot (from traceability matrix)
| Status | Test cases |
|---|---:|
| Passed | 23 |
| Failed | 1 (DEF-014: second failed face match does not route to manual KYC, **High**) |
| In progress | 1 |
| Not started | 1 (Could-have US-15) |

**Go/no-go recommendation:** conditional **GO** once DEF-014 is fixed and retested, because it affects a KYC control.
