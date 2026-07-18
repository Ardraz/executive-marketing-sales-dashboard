# ==========================================================
# DEVELOPMENT_GUIDE.md
# Executive Marketing & Sales Dashboard
# ==========================================================

Version         : 1.0.0
Status          : ACTIVE
Last Updated    : Sprint 18.3.2

---

# 1. PURPOSE

This guide explains how developers should work on the project.

It is intended for

- Project Owner
- Contributors
- Future Developers
- AI Assistants

This document defines

- Development workflow
- Coding standards
- Folder responsibilities
- Git workflow
- Sprint workflow
- Testing workflow
- Documentation workflow

Every contributor should read this guide before modifying the project.

---

# 2. DEVELOPMENT PRINCIPLES

The project follows several engineering principles.

Primary Principles

✓ Simplicity

✓ Readability

✓ Maintainability

✓ Reusability

✓ Documentation First

✓ Small Incremental Changes

✓ Architecture Stability

The project prioritizes long-term maintainability over short-term speed.

---

# 3. REQUIRED SOFTWARE

Minimum Requirements

Python

3.12+

Recommended IDE

Visual Studio Code

Operating System

Windows 11

Recommended Extensions

Python

Pylance

Black Formatter

GitLens

Markdown All in One

Power BI Desktop

Git

Latest Stable Version

---

# 4. PROJECT STRUCTURE

Project Root

│

├── docs/

├── src/

├── tests/

├── data/

├── reports/

├── requirements.txt

├── README.md

└── main.py

Every folder has a single responsibility.

Refer to ARCHITECTURE.md for detailed explanations.

---

# 5. ENVIRONMENT SETUP

Clone Repository

git clone <repository-url>

Change Directory

cd ExecutiveMarketingDashboard

Create Virtual Environment

python -m venv .venv

Activate

Windows

.venv\Scripts\activate

Linux

source .venv/bin/activate

Upgrade pip

python -m pip install --upgrade pip

Install Dependencies

pip install -r requirements.txt

Verify Installation

python --version

pip list

---

# 6. RUNNING THE APPLICATION

Execute

python main.py

Expected Flow

Load Configuration

↓

Generate Data

↓

Validate

↓

Run EDQE

↓

Generate Reports

↓

Export Data

↓

Power BI

Successful execution should complete without exceptions.

---

# 7. DIRECTORY RESPONSIBILITIES

docs/

Project documentation only.

Never store executable code.

----------------------------------------------------------

src/

Application source code.

----------------------------------------------------------

tests/

Unit and integration tests.

----------------------------------------------------------

data/

Generated datasets.

Lookup files.

Templates.

----------------------------------------------------------

reports/

Generated reports.

Console output

HTML

Excel

JSON

PDF

---

# 8. DEVELOPMENT WORKFLOW

Every new feature follows the same workflow.

Requirement

↓

Design

↓

Implementation

↓

Testing

↓

Documentation

↓

Review

↓

Commit

↓

Git Tag (Milestone)

Skipping documentation updates is prohibited.

---

# 9. CODING STANDARDS

General

Use meaningful names.

Keep functions short.

Avoid duplicated logic.

Prefer composition over duplication.

Maximum Function Length

Approximately 50 lines.

Maximum Class Length

Only when justified.

Avoid deeply nested logic.

Prefer early returns.

---

# 10. NAMING CONVENTIONS

Files

snake_case.py

Variables

snake_case

Functions

snake_case()

Classes

PascalCase

Constants

UPPER_CASE

Private Helpers

_prefix()

Maintain naming consistency throughout the project.

---

# 11. PYTHON STYLE GUIDE

Formatting

Black

Indentation

4 spaces

Encoding

UTF-8

Line Length

Black default

Imports

Standard Library

↓

Third Party

↓

Project Modules

Unused imports should be removed.

---

# 12. COMMENTS

Use comments only when necessary.

Good

Explain WHY.

Bad

Explain WHAT.

Example

Good

# Prevent duplicate customer IDs

Bad

# Increment i

Documentation should replace unnecessary comments.

---

# ==========================================================
# 13. GIT WORKFLOW
# ==========================================================

The project follows a simplified Git workflow suitable for a single
developer while remaining compatible with future team collaboration.

Development Flow

Requirement

↓

Implementation

↓

Testing

↓

Documentation Update

↓

Git Commit

↓

Milestone Review

↓

Git Tag

↓

Next Sprint

Every completed feature should be committed before starting a new one.

---

# 14. BRANCH STRATEGY

Current Strategy

main

The current project uses a single stable branch.

Future Strategy

main

↓

develop

↓

feature/*

↓

hotfix/*

Branch Purpose

main

Stable production-ready code.

develop

Integration branch.

feature/*

Individual feature development.

hotfix/*

Urgent production fixes.

For the current development stage, all work is performed directly on
the main branch.

---

# 15. COMMIT MESSAGE CONVENTION

Commit messages should be concise and descriptive.

Preferred Format

<type>: <description>

Examples

feat: add html report builder

feat: implement audit session

fix: resolve duplicate key validation

docs: update architecture documentation

refactor: simplify report pipeline

style: apply black formatter

test: add audit unit tests

chore: update dependencies

Avoid vague commit messages such as

update

fix

change

improvement

---

# 16. SPRINT WORKFLOW

Each sprint should follow the same lifecycle.

Planning

↓

Design

↓

Implementation

↓

Testing

↓

Documentation

↓

Review

↓

Sprint Complete

↓

Next Sprint

Every sprint should produce

✓ Working Code

✓ Updated Documentation

✓ Stable Repository

---

# 17. CODE REVIEW CHECKLIST

Before considering a feature complete, verify the following.

General

✓ Code compiles successfully.

✓ No runtime errors.

✓ Functions remain readable.

✓ Naming conventions followed.

✓ No duplicated logic.

Architecture

✓ Architecture Freeze respected.

✓ Single Source of Truth preserved.

✓ No circular dependencies.

✓ Responsibilities remain isolated.

Documentation

✓ PROJECT_CONTEXT updated.

✓ CHANGELOG updated.

✓ ROADMAP updated.

✓ DEVELOPMENT_GUIDE updated (if applicable).

✓ Comments remain accurate.

---

# 18. BLACK FORMATTER

The project uses Black as the official formatter.

Format Entire Project

python -m black src

Format Single File

python -m black main.py

Check Version

python -m black --version

Black formatting should be applied before every commit.

Manual formatting should be avoided whenever possible.

---

# 19. IMPORT ORGANIZATION

Imports should follow this order.

Standard Library

↓

Third-party Libraries

↓

Project Modules

Example

import os
from pathlib import Path

import pandas as pd

from src.edqe.audit_runner import AuditRunner

Avoid wildcard imports.

Example

Bad

from module import *

Good

from module import AuditRunner

---

# 20. TESTING STRATEGY

Testing occurs at multiple levels.

Unit Test

Individual function.

↓

Module Test

Entire module.

↓

Integration Test

Interaction between modules.

↓

End-to-End Test

Complete application.

Every new feature should be tested before merging.

---

# 21. BUG FIX WORKFLOW

Every bug follows the same process.

Identify

↓

Reproduce

↓

Fix

↓

Test

↓

Review

↓

Document

↓

Commit

Avoid implementing fixes without reproducing the issue first.

---

# 22. ERROR HANDLING

Expected errors should be handled gracefully.

Unexpected errors should fail loudly.

Good

Raise informative exceptions.

Bad

except:
    pass

Never suppress exceptions without a valid reason.

Error messages should help identify the root cause.

---

# 23. LOGGING GUIDELINES

Future versions will introduce centralized logging.

Recommended Log Levels

DEBUG

Development diagnostics.

INFO

Normal execution.

WARNING

Recoverable issues.

ERROR

Operation failed.

CRITICAL

Application cannot continue.

Avoid using print() for diagnostic output in production code.

---

# 24. RELEASE WORKFLOW

A release should only occur after completing the following.

Development Complete

↓

Testing Complete

↓

Documentation Updated

↓

Architecture Review

↓

Git Commit

↓

Git Tag

↓

Release

Never create a release from untested code.

---
# ==========================================================
# 25. ADDING A NEW GENERATOR
# ==========================================================

Every new generator must follow the existing project architecture.

Workflow

Business Requirement

↓

Design Dataset

↓

Define Business Rules

↓

Implement Generator

↓

Validate Output

↓

Run EDQE

↓

Update Documentation

Example

src/generators/

    dim_supplier_generator.py

    fact_inventory_generator.py

Requirements

✓ Return pandas DataFrame

✓ Deterministic when RANDOM_SEED is used

✓ No report generation

✓ No audit execution

✓ No export logic

Generators should only generate data.

---

# 26. ADDING A NEW AUDIT MODULE

Audit modules are independent validation components.

Directory

src/edqe/audits/

Example

duplicate_customer_audit.py

Responsibilities

✓ Validate data

✓ Produce AuditResult

✓ Never modify DataFrame

✓ Never generate reports

Workflow

Receive DataFrame

↓

Execute Validation

↓

Create AuditResult

↓

Return Result

Every audit must remain independent from other audits.

---

# 27. ADDING A NEW REPORT BUILDER

Reports are presentation components.

Directory

src/edqe/reports/

Example

html_report.py

excel_report.py

json_report.py

Responsibilities

✓ Read AuditSession

✓ Format Output

✓ Export Report

Must Never

✗ Execute audits

✗ Validate data

✗ Modify AuditSession

Every report builder must produce the same information presented in a
different format.

---

# 28. ADDING BUSINESS RULES

Business rules belong only inside

src/business/

Examples

Customer Status

Campaign Probability

Sales Conversion

Product Pricing

Inventory Logic

Business rules must never be duplicated inside generators or reports.

Single Source of Truth must always be preserved.

---

# 29. ADDING CONFIGURATION

Application configuration belongs inside

src/core/

Examples

config.py

constants.py

paths.py

environment.py

Avoid hardcoded values inside source code.

Good

OUTPUT_FOLDER

Bad

"C:/Reports"

Configuration should remain centralized.

---

# 30. WRITING UNIT TESTS

Every important module should have a corresponding unit test.

Directory

tests/

Example

tests/

    test_generator.py

    test_audit_runner.py

    test_report_builder.py

Suggested Structure

Arrange

↓

Act

↓

Assert

Each test should verify one behavior only.

---

# 31. EDQE COMPATIBILITY

Every new feature must remain compatible with the Enterprise Data
Quality Engine.

Checklist

✓ DataFrame schema respected

✓ TABLE_RULES updated

✓ AuditRunner unchanged

✓ AuditSession preserved

✓ ReportBuilder compatible

If compatibility cannot be maintained, the proposal must undergo an
architecture review before implementation.

---

# 32. ARCHITECTURE FREEZE COMPLIANCE

Architecture Freeze protects the project's core framework.

Protected Components

AuditRunner

AuditSession

AuditResult

AuditScore

TABLE_RULES

ReportBuilder Interface

Changes to these components require explicit approval.

Improvements should preferably be implemented through extension rather
than modification.

---

# 33. DOCUMENTATION REQUIREMENTS

Documentation is part of every feature.

Whenever a new feature is completed, review the following documents.

PROJECT_CONTEXT.md

ROADMAP.md

CHANGELOG.md

ARCHITECTURE.md

VERSION_HISTORY.md

DEVELOPMENT_GUIDE.md

README.md

Documentation should never lag behind the source code.

---

# 34. FILE ORGANIZATION

Keep project files organized.

Recommended Structure

src/

docs/

tests/

data/

reports/

assets/

scripts/

Avoid placing temporary files inside source directories.

Temporary artifacts should be removed before committing.

---

# 35. CODE REUSE GUIDELINES

Prefer reusable components over duplicated implementations.

Good

Shared utility function

↓

Multiple callers

Bad

Copy

↓

Paste

↓

Modify

Whenever duplicate logic is discovered, consider extracting it into a
shared module.

---

# 36. PERFORMANCE GUIDELINES

Optimize only after correctness has been achieved.

Priority

Correctness

↓

Readability

↓

Maintainability

↓

Performance

Future optimization opportunities

- Parallel audit execution

- Cached metadata

- Vectorized DataFrame operations

- Lazy report generation

Premature optimization should be avoided.

---
# ==========================================================
# 37. TROUBLESHOOTING GUIDE
# ==========================================================

The following table lists common development issues and their suggested
solutions.

----------------------------------------------------------

Problem

Virtual environment cannot be activated.

Possible Cause

Incorrect activation command.

Recommended Solution

Windows

.venv\Scripts\activate

Linux

source .venv/bin/activate

----------------------------------------------------------

Problem

ModuleNotFoundError

Possible Cause

Missing dependency.

Recommended Solution

pip install -r requirements.txt

----------------------------------------------------------

Problem

ImportError

Possible Cause

Incorrect project structure.

Recommended Solution

Verify project root and import statements.

----------------------------------------------------------

Problem

Black formatting failed.

Possible Cause

Syntax error.

Recommended Solution

Resolve syntax errors before running Black.

----------------------------------------------------------

Problem

Audit failed unexpectedly.

Possible Cause

Invalid schema.

Recommended Solution

Verify TABLE_RULES and DataFrame structure.

---

# 38. COMMON DEVELOPMENT MISTAKES

The following mistakes should be avoided.

✗ Duplicating business rules.

✗ Hardcoding configuration values.

✗ Editing protected architecture components without approval.

✗ Skipping documentation updates.

✗ Ignoring formatter output.

✗ Introducing circular dependencies.

✗ Mixing business logic with presentation logic.

✗ Modifying DataFrames inside audit modules.

✗ Writing reports that perform validation.

When in doubt, review ARCHITECTURE.md before making structural changes.

---

# 39. DEPENDENCY UPDATE POLICY

Dependencies should remain minimal and intentional.

Before adding a new package, evaluate whether it:

✓ Improves maintainability.

✓ Reduces implementation complexity.

✓ Is actively maintained.

✓ Has a permissive license.

✓ Is compatible with the current Python version.

Dependency updates should be tested before being committed.

Unused dependencies should be removed periodically.

---

# 40. CODE CLEANUP CHECKLIST

Before marking a task as complete, verify the following.

✓ Remove unused imports.

✓ Remove dead code.

✓ Remove temporary debugging statements.

✓ Remove commented-out code.

✓ Apply Black formatting.

✓ Verify naming consistency.

✓ Confirm documentation accuracy.

✓ Ensure no TODO items remain unintentionally.

A clean repository is easier to maintain and review.

---

# 41. PRE-COMMIT CHECKLIST

Every commit should satisfy the following checklist.

General

✓ Code executes successfully.

✓ No syntax errors.

✓ Black formatting applied.

✓ Imports organized.

✓ Tests passed.

Architecture

✓ No Architecture Freeze violations.

✓ SSOT preserved.

✓ Folder responsibilities respected.

Documentation

✓ Relevant documents updated.

✓ CHANGELOG reviewed.

✓ README updated if necessary.

Only commit code after all applicable checks have been completed.

---

# 42. RELEASE CHECKLIST

Before creating an official release, verify the following.

Code

✓ Stable implementation.

✓ No known critical defects.

✓ All planned features completed for the milestone.

Testing

✓ Unit testing completed.

✓ Integration testing completed.

✓ End-to-end execution verified.

Documentation

✓ PROJECT_CONTEXT.md

✓ ARCHITECTURE.md

✓ ROADMAP.md

✓ CHANGELOG.md

✓ VERSION_HISTORY.md

✓ DEVELOPMENT_GUIDE.md

✓ README.md

Repository

✓ Clean commit history.

✓ Git tag prepared.

✓ Release notes completed.

---

# 43. DAILY DEVELOPMENT ROUTINE

A recommended daily workflow.

Start Development

↓

Pull Latest Changes

↓

Implement Feature

↓

Run Application

↓

Execute EDQE

↓

Review Output

↓

Run Formatter

↓

Update Documentation

↓

Commit Changes

↓

Push Repository

Maintaining a consistent routine improves development quality and reduces
integration issues.

---

# 44. AI ASSISTANT GUIDELINES

AI assistants may be used to improve productivity but must follow the
project's engineering standards.

AI assistants should

✓ Respect Architecture Freeze.

✓ Preserve the Single Source of Truth (SSOT).

✓ Maintain folder responsibilities.

✓ Follow naming conventions.

✓ Produce readable code.

✓ Recommend documentation updates when applicable.

AI assistants must not

✗ Introduce architectural redesign without approval.

✗ Duplicate business logic.

✗ Bypass validation workflows.

✗ Remove documentation without justification.

All AI-generated code should be reviewed before acceptance.

---

# 45. MAINTENANCE POLICY

This guide should be reviewed whenever one of the following occurs.

- A new development workflow is introduced.

- Coding standards are revised.

- A new architectural principle is adopted.

- A new tool becomes part of the standard development process.

Minor feature additions generally do not require changes to this guide.

Whenever DEVELOPMENT_GUIDE.md is updated, consider reviewing the
following documents for consistency.

- PROJECT_CONTEXT.md

- ARCHITECTURE.md

- ROADMAP.md

- CHANGELOG.md

- VERSION_HISTORY.md

- README.md

---

# 46. QUICK REFERENCE

Common Commands

Create Virtual Environment

python -m venv .venv

Activate (Windows)

.venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Run Application

python main.py

Run Formatter

python -m black src

Format Single File

python -m black main.py

Run Tests

pytest

Update Dependencies (optional)

pip install --upgrade -r requirements.txt

These commands represent the most frequently used operations during
development.

---

# 47. DEVELOPMENT SUMMARY

The project follows a documentation-first and architecture-driven
development approach.

Core Principles

✓ Modular Architecture

✓ Enterprise Data Quality Engine (EDQE)

✓ Single Source of Truth (SSOT)

✓ Architecture Freeze

✓ Documentation-First Development

✓ Small Incremental Improvements

✓ Consistent Coding Standards

✓ Reusable Components

✓ Professional Git Workflow

✓ Long-Term Maintainability

By following this guide, contributors can extend the project while
preserving code quality, architectural integrity, and documentation
consistency.

---

# ==========================================================
# END OF DOCUMENT
# DEVELOPMENT_GUIDE.md
# Version 1.0.0
# ==========================================================