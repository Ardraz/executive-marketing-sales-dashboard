# ==========================================================
# AI_BOOTSTRAP.md
# Executive Marketing & Sales Dashboard
# ==========================================================

Version         : 1.0.0
Status          : ACTIVE
Purpose         : AI Onboarding Document
Priority        : HIGHEST

==========================================================
IMPORTANT
==========================================================

This document MUST be read FIRST before reading any other
documentation or source code.

Its purpose is to onboard any AI assistant into the project
quickly and consistently.

After reading this document, continue reading the remaining
documentation in the order specified below.

==========================================================
PROJECT OVERVIEW
==========================================================

Project Name

Executive Marketing & Sales Dashboard

Project Type

Enterprise Python Application

Primary Goal

Generate realistic synthetic business datasets,
validate them using the Enterprise Data Quality Engine (EDQE),
and produce professional reports suitable for Power BI dashboards.

Core Technologies

Python

Pandas

Power BI

Enterprise Data Quality Engine (EDQE)

==========================================================
PROJECT OBJECTIVES
==========================================================

The project has five primary objectives.

1.

Generate enterprise-quality synthetic datasets.

2.

Validate every generated dataset using EDQE.

3.

Produce professional audit reports.

4.

Create Power BI-ready datasets.

5.

Serve as a portfolio-quality enterprise application.

==========================================================
CURRENT PROJECT STATUS
==========================================================

Current Architecture

Enterprise Modular Architecture

Architecture Status

Architecture Freeze ACTIVE

Development Model

Documentation First

Single Source of Truth

ENABLED

Current Development Phase

Reporting Framework

Current Version

v0.4.0 (Development)

Target Release

v1.0.0

==========================================================
NON-NEGOTIABLE RULES
==========================================================

The following rules MUST always be respected.

✓ Architecture Freeze

✓ Single Source of Truth (SSOT)

✓ Documentation First

✓ Modular Architecture

✓ Low Coupling

✓ High Cohesion

✓ Small Incremental Improvements

✓ Functional Separation

Core framework components should not be redesigned without
explicit approval.

==========================================================
PROTECTED COMPONENTS
==========================================================

The following components are considered stable.

AuditRunner

AuditSession

AuditResult

AuditScore

TABLE_RULES

ReportBuilder Interface

These components may only be modified when explicitly required.

Otherwise, proposed improvements should be recorded
under Improvement V2.

==========================================================
DOCUMENT READING ORDER
==========================================================

Read documents in the following order.

1.

AI_BOOTSTRAP.md

↓

2.

PROMPT_FOR_NEXT_SESSION.md

↓

3.

AI_DEVELOPMENT_RULES.md

↓

4.

PROJECT_CONTEXT.md

↓

5.

ARCHITECTURE.md

↓

6.

DEVELOPMENT_GUIDE.md

↓

7.

ROADMAP.md

↓

8.

CHANGELOG.md

↓

9.

VERSION_HISTORY.md

↓

10.

MILESTONE_GIT.md

↓

11.

README.md

Do NOT begin modifying source code before understanding
the architecture.

==========================================================
SOURCE CODE READING ORDER
==========================================================

After documentation has been read,
inspect source code in the following order.

main.py

↓

src/core/

↓

src/business/

↓

src/generators/

↓

src/validators/

↓

src/edqe/

↓

src/pipeline/

↓

src/reports/

↓

tests/

Only inspect directories that are relevant to the current sprint.

==========================================================
AI WORKFLOW
==========================================================

Every development session should follow the same workflow.

Read Bootstrap

↓

Read Documentation

↓

Inspect Current Code

↓

Understand Current Sprint

↓

Plan Changes

↓

Implement

↓

Test

↓

Update Documentation

↓

Review

↓

Complete Sprint

Never skip documentation review.

==========================================================
WHEN MODIFYING CODE
==========================================================

Before changing any file, verify.

✓ Architecture remains unchanged.

✓ Responsibilities remain separated.

✓ SSOT preserved.

✓ No duplicated business logic.

✓ Documentation remains synchronized.

==========================================================
WHEN ADDING NEW FEATURES
==========================================================

Always prefer extension over modification.

Examples

Good

Add new Audit Module.

Add new Report Builder.

Add new Generator.

Bad

Modify AuditRunner unnecessarily.

Modify AuditSession unnecessarily.

Duplicate existing business logic.

==========================================================
CURRENT DEVELOPMENT PRIORITY
==========================================================

Follow the roadmap defined inside

ROADMAP.md

and

PROMPT_FOR_NEXT_SESSION.md

Do NOT invent new milestones.

Complete the current milestone before starting
the next one.

==========================================================
EXPECTED AI BEHAVIOR
==========================================================

The AI assistant should

✓ Follow project architecture.

✓ Respect Architecture Freeze.

✓ Produce maintainable code.

✓ Produce readable code.

✓ Keep documentation synchronized.

✓ Suggest improvements when appropriate.

The AI assistant should NOT

✗ Perform unnecessary refactoring.

✗ Change architecture without approval.

✗ Duplicate business logic.

✗ Ignore project documentation.

==========================================================
SESSION START CHECKLIST
==========================================================

Before writing any code verify

□ Documentation has been read.

□ Current sprint identified.

□ Current milestone identified.

□ Architecture understood.

□ Protected components identified.

□ Target files identified.

Only after all items are complete should implementation begin.

==========================================================
SESSION END CHECKLIST
==========================================================

Before finishing the session verify

□ Code implemented.

□ Tests completed.

□ Documentation updated.

□ Changelog updated.

□ Roadmap reviewed.

□ Prompt for next session updated.

□ Sprint completed.

==========================================================
QUICK SUMMARY
==========================================================

Project

Executive Marketing & Sales Dashboard

Architecture

Enterprise Modular Architecture

Validation

Enterprise Data Quality Engine

Reporting

Console

HTML

Excel

Future

JSON

PDF

Power BI

Target

Enterprise-grade portfolio project.

==========================================================
FINAL INSTRUCTION
==========================================================

Every new AI session MUST begin with the following process.

1.

Read AI_BOOTSTRAP.md completely.

2.

Read all required documentation.

3.

Understand current sprint.

4.

Understand architecture.

5.

Inspect relevant source code.

6.

Create an implementation plan.

7.

Implement incrementally.

8.

Update documentation.

9.

Prepare the next session.

Never skip this workflow.

# ==========================================================
# END OF DOCUMENT
# AI_BOOTSTRAP.md
# Version 1.0.0
# ==========================================================