# User Stories & Acceptance Criteria

Stories follow **INVEST** and the format *As a … I want … so that …*. Acceptance criteria are written in **Gherkin** (Given / When / Then). Priority uses **MoSCoW**; estimates are story points agreed in refinement.

## Epics
| Epic | Description | Business req. |
|---|---|---|
| E1 | Online application | BR-01 |
| E2 | Identity & compliance checks | BR-02, BR-08 |
| E3 | Automated credit decisioning | BR-03, BR-08 |
| E4 | Underwriter workbench | BR-04 |
| E5 | Contracting, notifications & reporting | BR-05, BR-06, BR-07 |

## Backlog
| ID | Epic | User story | MoSCoW | Pts | FR |
|---|---|---|---|---:|---|
| US-01 | E1 | As an **applicant**, I want to apply for a loan online so that I don't have to visit a branch | Must | 8 | FR-01 |
| US-02 | E1 | As an **applicant**, I want to save my application and resume later so that I don't lose progress | Must | 5 | FR-01 |
| US-03 | E1 | As an **existing customer**, I want my details pre-filled so that applying is faster | Should | 5 | FR-02 |
| US-04 | E1 | As an **applicant**, I want instant feedback on invalid fields so that I submit a complete application | Must | 3 | FR-03 |
| US-05 | E2 | As an **applicant**, I want to verify my identity with my phone camera so that I don't need to bring documents in person | Must | 8 | FR-04 |
| US-06 | E2 | As a **compliance officer**, I want every applicant screened against sanctions/PEP lists so that we meet AML obligations | Must | 5 | FR-05 |
| US-07 | E3 | As an **applicant**, I want to consent to a credit check digitally so that my application can be assessed immediately | Must | 3 | FR-06 |
| US-08 | E3 | As an **applicant**, I want to verify my income by connecting my bank account so that I don't have to upload payslips | Must | 8 | FR-07 |
| US-09 | E3 | As **Lending Ops**, I want low-risk applications decided automatically so that applicants get a same-day answer | Must | 13 | FR-08 |
| US-10 | E3 | As a **credit risk manager**, I want to adjust rule thresholds with maker-checker approval so that policy changes don't need a release | Should | 8 | FR-09 |
| US-11 | E4 | As an **underwriter**, I want referred applications in a queue ordered by SLA so that I work on the most urgent first | Must | 5 | FR-10 |
| US-12 | E4 | As an **underwriter**, I want all application data on one screen so that I can decide without switching systems | Must | 8 | FR-11 |
| US-13 | E4 | As an **underwriter**, I want to request extra documents in-system so that I don't have to email applicants | Should | 5 | FR-12 |
| US-14 | E5 | As an **applicant**, I want email/SMS updates at each stage so that I know where my application is | Should | 5 | FR-13 |
| US-15 | E5 | As an **applicant**, I want to see my application status online so that I don't have to call the bank | Could | 5 | FR-14 |
| US-16 | E5 | As an **approved applicant**, I want to e-sign my agreement so that I get my funds quickly | Must | 5 | FR-15 |
| US-17 | E5 | As **Lending Ops**, I want signed loans sent to core banking automatically so that nobody re-keys them | Must | 8 | FR-16 |
| US-18 | E5 | As the **Head of Lending**, I want a live pipeline dashboard so that I can manage SLAs and conversion | Should | 8 | FR-17, FR-18 |

**MoSCoW split:** Must 12 · Should 5 · Could 1 · Won't (this release): native apps, mortgages

---

## Detailed acceptance criteria (selected stories)

### US-02: Save and resume application
```gherkin
Feature: Save and resume loan application

  Scenario: Applicant saves a partially completed application
    Given I am an applicant who has completed steps 1 and 2 of 5
    When I click "Save and continue later"
    Then my progress is saved
    And I receive an email with a secure resume link valid for 30 days

  Scenario: Applicant resumes a saved application
    Given I have a saved application less than 30 days old
    When I open the resume link and verify with a one-time passcode
    Then I am returned to step 3 with steps 1–2 pre-populated

  Scenario: Resume link has expired
    Given my saved application is more than 30 days old
    When I open the resume link
    Then I see a message that the application has expired
    And I am offered the option to start a new application
```

### US-05: Digital identity verification
```gherkin
Feature: eKYC identity verification

  Scenario: Successful verification
    Given I have entered my personal details
    When I photograph a valid government ID and take a live selfie
    And the provider returns "document authentic" and "face match ≥ 90%"
    Then my identity status is set to "Verified"
    And I proceed to the credit consent step

  Scenario: Face match below threshold
    Given the provider returns a face match below 90%
    Then I am allowed one retry
    And if the retry also fails, the application is referred to manual KYC review

  Scenario: Expired document
    Given my ID document has expired
    Then I see "Your document has expired. Please use a valid ID."
    And I cannot continue until a valid document is captured
```

### US-09: Automated credit decision
```gherkin
Feature: Rules-based auto-decisioning

  Background:
    Given identity is "Verified" and sanctions screening is "Clear"

  Scenario: Auto-approve low-risk application
    Given the bureau score is 720 or above
    And debt-to-income after the new loan is 35% or below
    And the requested amount is $25,000 or below
    When the decision engine runs
    Then the decision is "Approve" within 60 seconds
    And the rules fired are written to the audit log

  Scenario: Refer borderline application
    Given the bureau score is between 620 and 719
    When the decision engine runs
    Then the decision is "Refer"
    And the application is placed in the underwriter queue with a 24-hour SLA

  Scenario: Auto-decline outside policy
    Given the bureau score is below 620 OR there is an active default
    When the decision engine runs
    Then the decision is "Decline"
    And the applicant receives an adverse-action notice listing the main reasons
```

### US-11: SLA-prioritised underwriter queue
```gherkin
Feature: Underwriter queue

  Scenario: Queue ordered by SLA
    Given there are referred applications with different SLA deadlines
    When I open my queue
    Then applications are sorted by time remaining to SLA, soonest first
    And applications with under 4 hours remaining are highlighted red

  Scenario: Prevent double-working
    Given an underwriter has opened application A-1001
    When another underwriter views the queue
    Then A-1001 shows as "In review by <name>" and cannot be picked
```

### US-16: e-Signature
```gherkin
Feature: Electronic signature of loan agreement

  Scenario: Applicant signs agreement
    Given my loan is approved
    When I review the agreement and sign electronically
    Then the signed PDF is stored against the application
    And a copy is emailed to me
    And the loan is released for disbursement

  Scenario: Offer expires
    Given my approval was issued more than 14 days ago and I have not signed
    Then the offer is withdrawn and I am notified
```

## Definition of Ready
- Story has a clear user, need and value; acceptance criteria agreed with the Product Owner
- Dependencies identified; UX designs attached where relevant; estimated by the team

## Definition of Done
- Acceptance criteria pass; code reviewed; unit and integration tests pass
- Traceability matrix updated; Product Owner accepts in sprint review
