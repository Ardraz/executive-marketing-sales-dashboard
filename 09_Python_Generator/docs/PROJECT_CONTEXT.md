# ==========================================================
# PROJECT_CONTEXT.md
# Executive Marketing & Sales Dashboard
# ==========================================================

Version         : 2.0.0
Status          : ACTIVE DEVELOPMENT
Last Updated    : Sprint 18.3.2
Architecture    : Enterprise Modular Architecture
Development     : Architecture Freeze Enabled

---

# 1. EXECUTIVE SUMMARY

## Project Name

Executive Marketing & Sales Dashboard

## Project Type

Enterprise Portfolio Project

## Primary Objective

Develop a production-quality business intelligence solution consisting of:

- Synthetic Business Data Generator
- Enterprise Data Quality Engine (EDQE)
- Executive Reporting Framework
- Power BI Dashboard
- Professional Documentation
- Production-ready Python Project

The project is intended to demonstrate professional software engineering,
data engineering, business intelligence, and software architecture skills.

---

# 2. PROJECT GOALS

The project has several long-term objectives.

## Data Generation

Generate realistic synthetic business datasets that simulate an actual
marketing and sales organization.

Generated datasets include:

- Customer Dimension
- Product Dimension
- Campaign Dimension
- Sales Representative Dimension
- Date Dimension

Fact Tables

- Leads
- Advertising
- Sales

---

## Data Quality

Every generated dataset must pass Enterprise Data Quality Engine (EDQE)
before export.

Validation includes:

- Missing Values
- Duplicate Primary Keys
- Foreign Keys
- Future audit modules

---

## Reporting

Generate professional reports for:

- Console
- HTML
- Excel

Future

- JSON
- PDF

---

## Visualization

Datasets are consumed by Power BI for Executive Dashboard reporting.

---

# 3. CURRENT DEVELOPMENT STATUS

Current Sprint

Sprint 18.4

Current Focus

Professional HTML Report Builder

Overall Status

Architecture Stable

Core Framework Completed

Reporting Framework In Progress

---

# 4. PROJECT EVOLUTION

Phase 1

Project Foundation

Completed

Phase 2

Synthetic Data Generator

Completed

Phase 3

Enterprise Data Quality Engine

Completed

Phase 4

Reporting Framework

In Progress

Phase 5

Configuration & Logging

Planned

Phase 6

Plugin System

Planned

Phase 7

Production Release

Future

---

# 5. ARCHITECTURE OVERVIEW

Current architecture consists of three major layers.

+--------------------------------------------------+
|                 APPLICATION                      |
+--------------------------------------------------+

               Reporting Layer

Console Report

HTML Report

Excel Report

↓

Enterprise Data Quality Engine

Audit Runner

Audit Session

Audit Score

Audit Result

Audit Modules

↓

Synthetic Data Generator

Dimensions

Facts

↓

Excel Export

↓

Power BI

---

# 6. CORE COMPONENTS

The project currently consists of the following subsystems.

## Synthetic Data Generator

Responsible for generating realistic business datasets.

Current dimensions:

✓ Dim_Date

✓ Dim_Customer

✓ Dim_Product

✓ Dim_Campaign

✓ Dim_SalesRep

Current fact tables:

✓ Fact_Leads

✓ Fact_Ads

✓ Fact_Sales

---

## Enterprise Data Quality Engine (EDQE)

Responsible for validating all generated datasets before export.

Current modules:

✓ Missing Value Audit

✓ Duplicate Primary Key Audit

✓ Foreign Key Audit

Future modules include:

- Data Type Audit

- Range Validation

- Domain Validation

- Business Rule Validation

- Statistical Outlier Detection

---

## Reporting Framework

Responsible for presenting audit results.

Implemented

✓ ReportBuilder

✓ ConsoleReport

In Progress

HTML Report

Planned

Excel Report

JSON Report

PDF Report

---

# 7. TECHNOLOGY STACK

Programming Language

Python

Formatter

Black

Primary IDE

Visual Studio Code

Data Storage

Excel

Data Processing

Pandas

Visualization

Power BI

Version Control

Git

Repository

GitHub

Operating System

Windows 11

---

# 8. PROJECT STRUCTURE

Current project structure.

src/

    business/

    core/

    data/

    generators/

    pipeline/

    validators/

    utils/

    edqe/

        audits/

        reports/

        audit_result.py

        audit_score.py

        audit_session.py

        audit_runner.py

        audit_rules.py

# ==========================================================
# 9. FOLDER RESPONSIBILITIES
# ==========================================================

Every directory inside the project has a single responsibility.
This separation ensures maintainability, scalability, and clean architecture.

----------------------------------------------------------

src/business/

Purpose

Contains business rules and domain-specific logic.

Examples

- Business constants
- Business calculations
- Probability models
- Status mapping
- Validation rules based on business requirements

This folder MUST NOT contain:

- Export logic
- Data generation
- Presentation logic

----------------------------------------------------------

src/core/

Purpose

Contains project-wide configuration and shared settings.

Examples

- config.py
- Random seed
- Global constants
- File locations
- Output configuration

----------------------------------------------------------

src/data/

Purpose

Stores generated datasets, templates, and static resources.

Examples

- Excel output
- Sample datasets
- Lookup tables
- Reference files

----------------------------------------------------------

src/generators/

Purpose

Generate synthetic datasets.

Responsibilities

- Create Dimensions
- Create Fact Tables
- Generate realistic values
- Respect business rules
- Produce pandas DataFrame

Generators must never contain presentation logic.

----------------------------------------------------------

src/pipeline/

Purpose

Coordinate generation workflow.

Pipeline responsibilities

Generate

↓

Validate

↓

Audit

↓

Export

↓

Return DataFrame

Pipelines must remain lightweight.

Business calculations are prohibited.

----------------------------------------------------------

src/validators/

Purpose

Perform lightweight validation before EDQE execution.

Examples

- Empty dataframe
- Required columns
- Basic integrity checks

Complex validation belongs to EDQE.

----------------------------------------------------------

src/utils/

Purpose

General helper functions.

Examples

- Date utilities
- String utilities
- File utilities
- Logging helpers

Utilities must remain reusable.

----------------------------------------------------------

src/edqe/

Purpose

Enterprise Data Quality Engine.

This module validates every generated dataset before export.

It is independent from the synthetic data generators and can be reused by
other projects in the future.

---

# 10. EDQE ARCHITECTURE

The Enterprise Data Quality Engine (EDQE) is designed using a modular
architecture where audit execution is separated from presentation.

Execution Layer

AuditRunner

↓

Audit Modules

↓

AuditResult

↓

AuditScore

↓

AuditSession

↓

Presentation Layer

Console Report

HTML Report

Excel Report

This architecture minimizes coupling and simplifies future extensions.

---

# 11. CORE EDQE COMPONENTS

AuditRunner

Responsibilities

- Execute audit modules
- Collect audit results
- Build AuditSession
- Return execution summary

AuditRunner does not generate reports.

---

AuditSession

Purpose

Represents the complete audit execution.

AuditSession contains:

- Execution metadata
- Dataset information
- Audit results
- Audit score
- Execution statistics
- Execution timestamps
- Summary information

AuditSession is the primary execution object shared with report builders.

---

AuditResult

Purpose

Represents the outcome of a single audit.

Typical information includes

- Audit name
- Status
- Severity
- Message
- Recommendation
- Execution duration

Each audit produces exactly one AuditResult.

---

AuditScore

Purpose

Represents the overall quality score.

Typical metrics include

- Total audits
- Passed audits
- Failed audits
- Warning count
- Overall percentage
- Final grade

Future versions may support weighted scoring.

---

Audit Modules

Each audit is implemented as an independent module.

Current modules

✓ Base Audit

✓ Missing Value Audit

✓ Duplicate Primary Key Audit

✓ Foreign Key Audit

Future modules

- Data Type Audit
- Range Validation
- Domain Validation
- Null Percentage Audit
- Duplicate Record Audit
- Business Rule Audit
- Statistical Outlier Audit
- Referential Completeness Audit

Each module must follow the same interface and remain independent from
other audit modules.

---

# 12. REPORTING FRAMEWORK

Report generation is completely separated from audit execution.

Current implementation

✓ ReportBuilder

✓ ConsoleReport

In development

HTMLReport

Planned

ExcelReport

JSONReport

PDFReport

Every report builder receives an AuditSession as input.

Report builders must never execute audits.

---

# 13. TABLE_RULES METADATA

TABLE_RULES stores schema metadata used by the audit engine.

Metadata examples

- Required columns
- Primary key
- Foreign keys
- Expected data type
- Nullable columns

TABLE_RULES acts as the metadata registry for every dataset.

Future schema changes should only require updates to TABLE_RULES rather
than individual audit modules.

---

# 14. SINGLE SOURCE OF TRUTH (SSOT)

The project follows a strict Single Source of Truth policy.

Execution Results

AuditSession

Schema Metadata

TABLE_RULES

Presentation Layer

AuditSession
+
TABLE_RULES

Audit modules must never duplicate schema metadata internally.

This policy minimizes inconsistency and simplifies maintenance.

---

# 15. ARCHITECTURE FREEZE

Architecture Freeze is currently ACTIVE.

The following core components are considered stable.

- AuditRunner
- AuditSession
- AuditResult
- AuditScore
- TABLE_RULES

These components may only be modified when:

1. Fixing a confirmed defect.

2. Resolving a significant performance issue.

3. Supporting a mandatory architectural requirement.

Any proposed enhancement that is not mandatory shall be documented as
"Improvement V2" instead of modifying the current architecture.

---

# 16. DEVELOPMENT WORKFLOW

Every sprint follows a standardized engineering workflow.

Planning

↓

Architecture Review

↓

Implementation

↓

Testing

↓

Code Review

↓

Documentation

↓

Git Commit

↓

Git Tag (Milestone)

Documentation must always reflect the latest implementation before a
sprint is considered complete.

---

# ==========================================================
# 17. DEVELOPMENT HISTORY
# ==========================================================

The project has evolved through several major development phases.

----------------------------------------------------------

Phase 1
Project Foundation

Completed

Major Deliverables

✓ Project Initialization

✓ Configuration Management

✓ Folder Structure

✓ Development Standards

----------------------------------------------------------

Phase 2
Synthetic Business Data Generator

Completed

Dimensions

✓ Dim_Date

✓ Dim_Customer

✓ Dim_Product

✓ Dim_Campaign

✓ Dim_SalesRep

Fact Tables

✓ Fact_Leads

✓ Fact_Ads

✓ Fact_Sales

The generator now produces realistic synthetic datasets suitable for
Business Intelligence demonstrations.

----------------------------------------------------------

Phase 3
Enterprise Data Quality Engine (EDQE)

Completed

Major Deliverables

✓ Audit Framework

✓ AuditRunner

✓ AuditResult

✓ AuditScore

✓ AuditSession

✓ Missing Value Audit

✓ Duplicate Primary Key Audit

✓ Foreign Key Audit

✓ Generator Schema Verification

✓ TABLE_RULES Metadata Refactor

The EDQE framework is now stable and protected by the Architecture
Freeze policy.

----------------------------------------------------------

Phase 4
Reporting Framework

In Progress

Completed

✓ ReportBuilder

✓ ConsoleReport

Current Development

▶ HTML Report Builder

Planned

□ Excel Report

□ JSON Report

□ PDF Report

----------------------------------------------------------

Phase 5
Enterprise Infrastructure

Planned

Modules

□ Logging System

□ Configuration Manager

□ Plugin Loader

□ Report Configuration

□ Audit Configuration

----------------------------------------------------------

Phase 6
Production Release

Future

Target

Version 1.0.0

Production-ready portfolio application.

---

# 18. CURRENT MILESTONE

Current Version

v0.7.x

Current Sprint

Sprint 18.4

Current Focus

Professional HTML Report Builder

Overall Progress

Project Foundation

Completed

Synthetic Data Generator

Completed

Enterprise Data Quality Engine

Completed

Reporting Framework

In Progress

Production Readiness

In Progress

---

# 19. NEXT DEVELOPMENT TARGETS

Immediate Target

Sprint 18.4

Professional HTML Report

Next Targets

Sprint 18.5

Excel Report Builder

Sprint 18.6

Main Application Integration

Sprint 19

Logging Framework

Sprint 20

Configuration Framework

Sprint 21

Plugin Audit Framework

Long-Term Targets

REST API

CLI Interface

Cloud Storage Support

CI/CD Pipeline

Automated Testing

Docker Support

Package Distribution

---

# 20. IMPROVEMENT V2 BACKLOG

The following enhancements have been identified but intentionally
deferred to preserve the current Architecture Freeze.

Potential Improvements

- Weighted Audit Score

- Audit Categories

- Audit Severity Levels

- Rule-based Configuration

- Parallel Audit Execution

- Multi-threaded Validation

- Incremental Audit Execution

- Report Localization

- Dark Mode HTML Report

- Dashboard Theme System

- Interactive HTML Charts

- Historical Audit Comparison

- Audit Trend Analysis

- Plugin Marketplace

- Remote Configuration

No Improvement V2 item should modify the current architecture unless
explicitly approved by the project owner.

---

# 21. KEY TECHNICAL DECISIONS

The following architectural decisions are considered fundamental.

Decision 1

Synthetic Data Generator and EDQE remain independent modules.

Decision 2

Report generation is separated from audit execution.

Decision 3

AuditSession is the single source of truth for execution results.

Decision 4

TABLE_RULES is the single source of truth for schema metadata.

Decision 5

Report builders consume AuditSession but never execute audits.

Decision 6

Audit modules remain independent and reusable.

Decision 7

Business logic remains outside the reporting layer.

Decision 8

Architecture Freeze protects all core framework components.

These decisions should remain unchanged unless a major version redesign
is approved.

---

# 22. PROJECT QUALITY OBJECTIVES

The project aims to meet professional software engineering standards.

Primary Objectives

- Correctness

- Maintainability

- Readability

- Consistency

- Extensibility

- Scalability

- Reusability

- Testability

- Documentation Quality

- Portfolio Quality

Implementation quality always takes priority over development speed.

---

# 23. LONG-TERM VISION

The long-term objective is to transform the project into a complete
enterprise-grade data engineering portfolio.

The final application will demonstrate:

✓ Synthetic Business Data Generation

✓ Enterprise Data Quality Validation

✓ Professional Reporting Framework

✓ Power BI Executive Dashboard

✓ Clean Modular Architecture

✓ Production-quality Documentation

✓ Git Versioning Strategy

✓ Professional Development Workflow

The completed project should represent the quality and engineering
practices expected in a real-world business intelligence application.

---

# 24. DOCUMENT MAINTENANCE POLICY

This document must be reviewed after every completed sprint.

Review Checklist

✓ Development Status

✓ Sprint Progress

✓ Architecture Changes

✓ Completed Modules

✓ Planned Modules

✓ Technical Decisions

✓ Improvement V2 Backlog

✓ Version Information

If no project context has changed, the document version should remain
unchanged.

---

# ==========================================================
# END OF DOCUMENT
# PROJECT_CONTEXT.md
# Version 2.0.0
# ==========================================================