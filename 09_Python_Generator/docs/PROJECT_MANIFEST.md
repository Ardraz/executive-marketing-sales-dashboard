# ==========================================================
# PROJECT_MANIFEST.md
# Executive Marketing & Sales Dashboard
# ==========================================================

Version         : 1.0.0
Status          : ACTIVE
Purpose         : Master Project Index
Priority        : HIGH

==========================================================
PURPOSE
==========================================================

PROJECT_MANIFEST.md is the master index of the project.

Its purpose is to provide both developers and AI assistants with a
single entry point for understanding the project's structure,
documentation, source code organization, and development workflow.

This document answers four fundamental questions.

1.

What documents exist?

2.

What does each document contain?

3.

When should each document be read?

4.

Which source code should be inspected?

==========================================================
PROJECT OVERVIEW
==========================================================

Project Name

Executive Marketing & Sales Dashboard

Application Type

Enterprise Python Application

Primary Language

Python

Architecture

Enterprise Modular Architecture

Validation Framework

Enterprise Data Quality Engine (EDQE)

Visualization

Power BI

Current Version

v0.4.0

Architecture Status

Architecture Freeze ACTIVE

==========================================================
MASTER DOCUMENT INDEX
==========================================================

The following documents represent the official documentation
of the project.

----------------------------------------------------------

AI_BOOTSTRAP.md

Priority

★★★★★

Purpose

AI onboarding.

Read First

YES

----------------------------------------------------------

PROMPT_FOR_NEXT_SESSION.md

Priority

★★★★★

Purpose

Current sprint status.

Read Before Coding

YES

----------------------------------------------------------

AI_DEVELOPMENT_RULES.md

Priority

★★★★★

Purpose

Rules that AI must follow.

Read Before Coding

YES

----------------------------------------------------------

PROJECT_CONTEXT.md

Priority

★★★★★

Purpose

Project overview.

Business goals.

Current status.

----------------------------------------------------------

ARCHITECTURE.md

Priority

★★★★★

Purpose

Software architecture.

Layer responsibilities.

Design principles.

Protected components.

----------------------------------------------------------

DEVELOPMENT_GUIDE.md

Priority

★★★★★

Purpose

Developer handbook.

Workflow.

Coding standards.

Testing.

----------------------------------------------------------

ROADMAP.md

Priority

★★★★☆

Purpose

Future milestones.

Current development phase.

----------------------------------------------------------

CHANGELOG.md

Priority

★★★★☆

Purpose

History of notable changes.

----------------------------------------------------------

VERSION_HISTORY.md

Priority

★★★★☆

Purpose

Version evolution.

Sprint mapping.

Git history.

----------------------------------------------------------

MILESTONE_GIT.md

Priority

★★★☆☆

Purpose

Git tagging strategy.

Release milestones.

----------------------------------------------------------

BUSINESS_RULES.md

Priority

★★★★☆

Purpose

Business logic reference.

----------------------------------------------------------

SALES_RULES.md

Priority

★★★☆☆

Purpose

Sales-specific rules.

----------------------------------------------------------

README.md

Priority

★★★★☆

Purpose

Public repository overview.

==========================================================
DOCUMENT READING MATRIX
==========================================================

Scenario

New AI Session

Read

AI_BOOTSTRAP

↓

PROMPT_FOR_NEXT_SESSION

↓

AI_DEVELOPMENT_RULES

↓

PROJECT_CONTEXT

↓

ARCHITECTURE

↓

DEVELOPMENT_GUIDE

----------------------------------------------------------

Scenario

Bug Fix

Read

PROJECT_CONTEXT

↓

ARCHITECTURE

↓

Relevant Source Code

----------------------------------------------------------

Scenario

New Feature

Read

ROADMAP

↓

PROMPT_FOR_NEXT_SESSION

↓

ARCHITECTURE

↓

Relevant Modules

----------------------------------------------------------

Scenario

Architecture Review

Read

ARCHITECTURE

↓

PROJECT_CONTEXT

↓

CHANGELOG

↓

VERSION_HISTORY

----------------------------------------------------------

Scenario

Release

Read

CHANGELOG

↓

VERSION_HISTORY

↓

MILESTONE_GIT

==========================================================
PROJECT DIRECTORY MAP
==========================================================

project/

│

├── docs/

│

├── src/

│

├── tests/

│

├── data/

│

├── reports/

│

├── assets/

│

├── requirements.txt

│

├── README.md

│

└── main.py

==========================================================
SOURCE CODE RESPONSIBILITIES
==========================================================

main.py

Application entry point.

----------------------------------------------------------

src/business/

Business rules.

----------------------------------------------------------

src/core/

Configuration.

----------------------------------------------------------

src/data/

Datasets.

Templates.

----------------------------------------------------------

src/generators/

Synthetic dataset generation.

----------------------------------------------------------

src/pipeline/

Workflow orchestration.

----------------------------------------------------------

src/validators/

Basic validation.

----------------------------------------------------------

src/edqe/

Enterprise Data Quality Engine.

----------------------------------------------------------

src/utils/

Utility functions.

----------------------------------------------------------

tests/

Unit testing.

Integration testing.

==========================================================
DEPENDENCY FLOW
==========================================================

Business Rules

↓

Generators

↓

Validators

↓

EDQE

↓

Report Builders

↓

Export

↓

Power BI

Dependencies should always follow this direction.

Reverse dependencies are prohibited.

==========================================================
PROTECTED COMPONENTS
==========================================================

The following components are protected.

AuditRunner

AuditSession

AuditResult

AuditScore

TABLE_RULES

ReportBuilder Interface

These components may only be modified after architecture review.

==========================================================
DEVELOPMENT WORKFLOW
==========================================================

Requirement

↓

Planning

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

Git Tag

↓

Next Sprint

==========================================================
CURRENT DEVELOPMENT STATUS
==========================================================

Architecture

Stable

Current Phase

Reporting Framework

Current Milestone

Professional HTML Report

Target Version

v1.0.0

Architecture Freeze

ACTIVE

==========================================================
DEFINITION OF DONE
==========================================================

A task is considered complete only if

✓ Feature implemented

✓ Tested

✓ Documentation updated

✓ Architecture respected

✓ SSOT preserved

✓ Changelog updated

✓ Prompt updated

==========================================================
AI QUICK START
==========================================================

Step 1

Read AI_BOOTSTRAP.md

↓

Step 2

Read PROMPT_FOR_NEXT_SESSION.md

↓

Step 3

Read AI_DEVELOPMENT_RULES.md

↓

Step 4

Read PROJECT_CONTEXT.md

↓

Step 5

Read ARCHITECTURE.md

↓

Step 6

Inspect relevant source code

↓

Step 7

Implement

↓

Step 8

Update documentation

↓

Step 9

Prepare next session

==========================================================
PROJECT HEALTH CHECK
==========================================================

Before every sprint completion verify

□ Architecture unchanged

□ Documentation synchronized

□ Protected components preserved

□ Tests completed

□ Changelog updated

□ Roadmap reviewed

□ Next session prepared

==========================================================
FINAL NOTES
==========================================================

PROJECT_MANIFEST.md is the master navigation document for the
Executive Marketing & Sales Dashboard project.

Whenever new documentation is added or removed, this manifest
must be updated to keep the project index accurate.

Developers and AI assistants should consult this file whenever
they need to locate documentation, understand project structure,
or determine the correct workflow before making changes.

# ==========================================================
# END OF DOCUMENT
# PROJECT_MANIFEST.md
# Version 1.0.0
# ==========================================================