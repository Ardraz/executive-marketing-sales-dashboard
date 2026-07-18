# PROMPT_FOR_NEXT_SESSION.md

# ==========================================================
# PROMPT FOR NEXT AI DEVELOPMENT SESSION
# Executive Marketing & Sales Dashboard
# ==========================================================

Hello.

You are joining an ongoing software engineering project.

Before writing any code,
you MUST read and understand all documentation
inside the docs folder.

The project documentation is the primary source of truth.

Do NOT rely on assumptions.

==========================================================
PROJECT DOCUMENTATION
==========================================================

Please read these files first
in the following order:

1.

PROJECT_CONTEXT.md

2.

AI_DEVELOPMENT_RULES.md

3.

ROADMAP.md

4.

BUSINESS_RULES.md

5.

DATA_DICTIONARY.md

6.

CHANGELOG.md

7.

MILESTONE_GIT.md

==========================================================
PROJECT OVERVIEW
==========================================================

Project Name

Executive Marketing & Sales Dashboard

Language

Python

Architecture

Functional Programming

Formatter

Black

Output

Excel Dataset

Visualization

Power BI

Current Status

The project has completed Sprint 15.

Current Sprint

Sprint 16

Fact_Sales

==========================================================
YOUR RESPONSIBILITIES
==========================================================

You are expected to act as:

Software Engineer

Python Developer

Data Engineer

Data Analyst

Code Reviewer

Documentation Engineer

You are NOT just a code generator.

Your objective is to build
a production-quality portfolio project.

==========================================================
MANDATORY RULES
==========================================================

Rule 1

Never assume
the content of any file.

If a file has not been provided,
ask for it first.

----------------------------------------------------------

Rule 2

Always preserve
the existing architecture.

Do not redesign the project.

----------------------------------------------------------

Rule 3

Respect Design Freeze.

Architecture changes are prohibited.

If you find a better solution,

document it as

Improvement V2

instead of changing
the existing implementation.

----------------------------------------------------------

Rule 4

Always provide COMPLETE FILES.

Never provide snippets.

If a file exceeds
the response length limit,

split the SAME FILE into:

Part 1

Part 2

Part 3

...

until the file is complete.

----------------------------------------------------------

Rule 5

Business rules belong in

business/

Configuration belongs in

core/config.py

Generators belong in

generators/

Pipelines belong in

pipeline/

Validation belongs in

validators/

----------------------------------------------------------

Rule 6

Do not duplicate business logic.

----------------------------------------------------------

Rule 7

Follow Black formatting.

----------------------------------------------------------

Rule 8

Keep naming convention consistent.

----------------------------------------------------------

Rule 9

Never refactor
working modules
unless explicitly requested.

----------------------------------------------------------

Rule 10

Every recommendation
must include
the technical reason.

==========================================================
DEVELOPMENT WORKFLOW
==========================================================

For every sprint

Review

↓

Planning

↓

Implementation

↓

Review

↓

Testing

↓

Documentation

↓

Git Milestone

==========================================================
AFTER EVERY SPRINT
==========================================================

Update

PROJECT_CONTEXT.md

ROADMAP.md

BUSINESS_RULES.md

CHANGELOG.md

DATA_DICTIONARY.md

MILESTONE_GIT.md

if there are changes.

==========================================================
WHEN YOU NEED ADDITIONAL INFORMATION
==========================================================

If you need any source code,

ask ONLY for
the required file.

Do not guess.

Do not invent.

Do not approximate.

==========================================================
WHEN REVIEWING CODE
==========================================================

Review from multiple perspectives:

Software Engineer

Python Developer

Data Engineer

Data Analyst

Code Reviewer

Performance

Maintainability

Scalability

Portfolio Quality

==========================================================
PROJECT OBJECTIVE
==========================================================

This project is intended to become
a professional portfolio project.

The quality target is comparable to
a production-ready business application.

Code quality,
architecture,
documentation,
consistency,
and maintainability
are more important
than writing code quickly.

==========================================================
STARTING INSTRUCTION
==========================================================

After reading
all documentation,

summarize your understanding
of the current project status.

Do not write any code yet.

First,

identify:

• Current Sprint

• Completed Modules

• Pending Modules

• Architecture

• Folder Structure

• Business Rules

• Dependencies

• Potential Risks

Wait for confirmation

before generating
the next source code.

==========================================================
# PROMPT FOR NEXT SESSION

## Project

Executive Marketing & Sales Dashboard

Synthetic Business Data Generator with Enterprise Data Quality Engine (EDQE)

---

# Current Development Status

Architecture Status:

✅ ARCHITECTURE FREEZE ENABLED

Core architecture must not be changed unless:

- Bug fix
- Significant performance improvement
- Mandatory requirement for a new feature

---

# Current Sprint

Completed:

Sprint 17.1
EDQE Framework

Sprint 17.2
Pipeline Refactor

Sprint 17.3
Export Manager

Sprint 17.4
Missing Value Audit

Sprint 17.5
Base Audit

Sprint 17.6
Duplicate Primary Key Audit

Sprint 17.7
Generator Schema Verification

Sprint 17.8
TABLE_RULES Metadata Refactor

Sprint 17.9
Foreign Key Audit

Sprint 18.0
Report Builder Base

Sprint 18.1
Console Report

Sprint 18.2
AuditSession

Sprint 18.3
AuditRunner Refactor

Sprint 18.3.1
Rich DataFrame Metadata

Sprint 18.3.2
AuditSession Enhancement

---

# Current EDQE Architecture

AuditResult
↓

AuditScore
↓

AuditSession
↓

Report Builders

Metadata (TABLE_RULES)

↓

Audit Engine

---

# Current Folder Structure

src/

edqe/

audit_result.py

audit_score.py

audit_session.py

audit_runner.py

audit_rules.py

audits/

base_audit.py

missing_value_audit.py

duplicate_audit.py

foreign_key_audit.py

reports/

__init__.py

report_builder.py

console_report.py

html_report.py (not implemented)

excel_report.py (not implemented)

templates/ (not implemented)

---

# Important Decisions

Architecture Freeze is active.

AuditSession is the single source of truth for execution results.

TABLE_RULES is the single source of truth for schema metadata.

Report layer is allowed to read:

- AuditSession
- TABLE_RULES

AuditRunner only executes audits.

Report builders are responsible for presentation.

---

# Next Sprint

Sprint 18.4

Professional HTML Report Builder

Implement:

src/edqe/reports/html_report.py

src/edqe/reports/templates/report.html

src/edqe/reports/templates/report.css

src/edqe/reports/templates/report.js

Requirements:

- Bootstrap 5
- Responsive Layout
- Professional Dashboard
- KPI Cards
- Progress Bar
- Audit Summary
- DataFrame Summary
- Audit Details
- Recommendations
- Footer
- Modern UI
- Clean Code

After HTML Report:

Sprint 18.5

Excel Report

Sprint 18.6

Main.py Integration

Sprint 19

Logging System

Sprint 20

Configuration System

Sprint 21

Plugin Audit System

---

# Development Rules

Always provide COMPLETE FILES.

Never provide snippets for modified files.

If a file is too large:

Part 1

Part 2

etc.

Never perform unnecessary refactoring.

Maintain Enterprise-level Clean Architecture.

Follow SOLID principles.

Keep code readable.

Keep naming consistent.

Minimize coupling.

Maximize maintainability.

Before changing architecture:

Evaluate carefully.

If Architecture Freeze would be violated:

Ask first.

Do not change automatically.

---

Continue development immediately from Sprint 18.4 without repeating previous discussions.
==========================================================