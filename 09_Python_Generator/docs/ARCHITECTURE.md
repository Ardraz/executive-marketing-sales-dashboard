# ==========================================================
# ARCHITECTURE.md
# Executive Marketing & Sales Dashboard
# ==========================================================

Version         : 1.0.0
Status          : ACTIVE
Last Updated    : Sprint 18.3.2

Architecture    : Enterprise Modular Architecture

---

# 1. PURPOSE

This document defines the complete software architecture of the
Executive Marketing & Sales Dashboard project.

It serves as the primary technical reference for:

- Software Developers
- AI Assistants
- Code Reviewers
- Future Contributors

This document explains how every major subsystem interacts and why
architectural decisions were made.

---

# 2. ARCHITECTURE OBJECTIVES

The architecture has been designed with the following objectives.

Primary Objectives

✓ Maintainability

✓ Scalability

✓ Reusability

✓ Testability

✓ Readability

✓ Separation of Concerns

✓ Low Coupling

✓ High Cohesion

✓ Enterprise Quality

The architecture always prioritizes long-term maintainability over
short-term implementation speed.

---

# 3. HIGH LEVEL SYSTEM ARCHITECTURE

+-------------------------------------------------------------+
|                  Executive Marketing Dashboard              |
+-------------------------------------------------------------+

                    Main Application
                           │
                           │
                           ▼
              Synthetic Data Generator
                           │
                           ▼
               Generated DataFrames
                           │
                           ▼
       Enterprise Data Quality Engine (EDQE)
                           │
                           ▼
                    Audit Session
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
         ▼                 ▼                 ▼
 Console Report      HTML Report      Excel Report
         │                 │                 │
         └─────────────────┼─────────────────┘
                           ▼
                     Output Reports
                           │
                           ▼
                     Power BI Dashboard

---

# 4. SYSTEM COMPONENTS

The application consists of four major subsystems.

----------------------------------------------------------

Subsystem 1

Synthetic Data Generator

Responsibilities

- Generate Dimensions

- Generate Fact Tables

- Produce realistic business datasets

- Apply business rules

- Produce validated DataFrames

Output

Pandas DataFrames

----------------------------------------------------------

Subsystem 2

Enterprise Data Quality Engine (EDQE)

Responsibilities

- Execute audit modules

- Validate generated datasets

- Produce audit results

- Calculate quality scores

- Build AuditSession

Output

AuditSession

----------------------------------------------------------

Subsystem 3

Reporting Framework

Responsibilities

- Read AuditSession

- Generate reports

- Present audit information

Supported Reports

✓ Console

▶ HTML

□ Excel

□ JSON

□ PDF

----------------------------------------------------------

Subsystem 4

Business Intelligence

Responsibilities

- Read exported datasets

- Build dashboards

- Create executive KPIs

- Produce visual analytics

Platform

Power BI

---

# 5. CORE ARCHITECTURAL PRINCIPLES

The project follows several fundamental software engineering principles.

----------------------------------------------------------

Principle 1

Single Responsibility Principle

Every module should have exactly one reason to change.

Examples

AuditRunner

Only executes audits.

ReportBuilder

Only builds reports.

Generator

Only generates datasets.

----------------------------------------------------------

Principle 2

Separation of Concerns

Generation

↓

Validation

↓

Audit

↓

Reporting

↓

Visualization

Each concern is implemented independently.

----------------------------------------------------------

Principle 3

Low Coupling

Modules communicate through well-defined interfaces.

A module should know as little as possible about other modules.

----------------------------------------------------------

Principle 4

High Cohesion

Related functionality is grouped together.

Example

All audit modules belong inside

src/edqe/audits/

----------------------------------------------------------

Principle 5

Extensibility

Adding a new audit or report should require minimal changes to the
existing framework.

---

# 6. PROJECT DIRECTORY ARCHITECTURE

src/

│

├── business/

├── core/

├── data/

├── generators/

├── pipeline/

├── validators/

├── utils/

│

└── edqe/

        audits/

        reports/

        audit_result.py

        audit_score.py

        audit_session.py

        audit_runner.py

        audit_rules.py

Every directory has a clearly defined responsibility.

---

# 7. DATA FLOW OVERVIEW

The application follows a strictly controlled processing pipeline.

Business Rules

↓

Synthetic Data Generation

↓

Validation

↓

Enterprise Audit

↓

AuditSession

↓

Report Builder

↓

Export

↓

Power BI

Every dataset must pass the EDQE layer before it is considered suitable
for reporting.

---

# 8. ARCHITECTURE LIFECYCLE

Project Startup

↓

Load Configuration

↓

Generate Data

↓

Validate Data

↓

Run EDQE

↓

Build AuditSession

↓

Generate Reports

↓

Export Files

↓

Open Power BI

This lifecycle should remain stable unless an architectural redesign is
approved.

---
# ==========================================================
# 9. LAYERED ARCHITECTURE
# ==========================================================

The project adopts a layered architecture to separate responsibilities
between business logic, data generation, validation, auditing,
reporting, and visualization.

+------------------------------------------------------+
|                Presentation Layer                    |
|  Console | HTML | Excel | JSON | PDF                |
+------------------------------------------------------+
                     ▲
                     │
+------------------------------------------------------+
|              Reporting Framework                     |
+------------------------------------------------------+
                     ▲
                     │
+------------------------------------------------------+
|      Enterprise Data Quality Engine (EDQE)           |
+------------------------------------------------------+
                     ▲
                     │
+------------------------------------------------------+
|        Validation & Processing Layer                 |
+------------------------------------------------------+
                     ▲
                     │
+------------------------------------------------------+
|      Synthetic Business Data Generator               |
+------------------------------------------------------+
                     ▲
                     │
+------------------------------------------------------+
|        Business Rules & Configuration                |
+------------------------------------------------------+

Each layer communicates only with its adjacent layer.

Cross-layer dependencies should be avoided.

---

# 10. DIRECTORY RESPONSIBILITIES

Every directory has a clearly defined responsibility.

----------------------------------------------------------

src/business/

Purpose

Business knowledge.

Contains:

- Business rules
- Domain calculations
- Probability models
- Lookup logic
- Status transitions

Must never contain:

- Export code
- Report code
- Audit code

----------------------------------------------------------

src/core/

Purpose

Global configuration.

Contains:

- config.py
- constants
- paths
- environment settings
- random seed

----------------------------------------------------------

src/data/

Purpose

Project data storage.

Contains:

- generated datasets
- templates
- lookup files
- sample data

----------------------------------------------------------

src/generators/

Purpose

Synthetic data generation.

Responsibilities

- Build dimensions

- Build fact tables

- Produce DataFrames

Generators must remain deterministic when RANDOM_SEED is used.

----------------------------------------------------------

src/pipeline/

Purpose

Coordinate the complete generation workflow.

Pipeline order

Generate

↓

Validate

↓

Audit

↓

Export

↓

Return

Pipeline modules should never perform business calculations.

----------------------------------------------------------

src/validators/

Purpose

Basic validation.

Examples

- Empty DataFrame

- Required Columns

- Basic Integrity

Enterprise validation belongs to EDQE.

----------------------------------------------------------

src/utils/

Purpose

Reusable helper functions.

Examples

- Date utilities

- File utilities

- String utilities

- Logging helpers

Utilities should never contain business logic.

----------------------------------------------------------

src/edqe/

Purpose

Enterprise Data Quality Engine.

This module validates every generated dataset before export.

It is intentionally isolated so that it can be reused in future
projects without depending on the synthetic generator.

---

# 11. EDQE INTERNAL ARCHITECTURE

The Enterprise Data Quality Engine follows a modular pipeline.

                     AuditRunner
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
 Missing Audit     Duplicate Audit   Foreign Key Audit
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                    AuditResult
                          │
                          ▼
                     AuditScore
                          │
                          ▼
                    AuditSession
                          │
                          ▼
                    Report Builders

Every audit executes independently.

The execution order does not affect report generation.

---

# 12. AUDIT EXECUTION PIPELINE

Each dataset follows the same audit lifecycle.

Receive DataFrame

↓

Load TABLE_RULES

↓

Execute Audit Modules

↓

Collect AuditResult

↓

Calculate AuditScore

↓

Build AuditSession

↓

Generate Reports

↓

Return AuditSession

This standardized pipeline ensures consistent audit behavior across all
datasets.

---

# 13. REPORTING PIPELINE

The reporting framework never executes business logic.

AuditSession

↓

Report Builder

↓

Console Report

HTML Report

Excel Report

↓

Output Files

↓

End User

Every report receives the same AuditSession object.

This guarantees consistent information across all report formats.

---

# 14. DATA OWNERSHIP

Each subsystem owns its own data.

Business Layer

Owns

Business Rules

----------------------------------------------------------

Generator

Owns

Generated DataFrames

----------------------------------------------------------

EDQE

Owns

Audit Results

Audit Scores

Audit Session

----------------------------------------------------------

Report Layer

Owns

Presentation only.

It must never modify audit results.

----------------------------------------------------------

Power BI

Owns

Visualization.

Power BI must never perform data validation.

---

# 15. DEPENDENCY RULES

Dependencies must always point downward.

Allowed

Generator

↓

EDQE

↓

Reports

↓

Power BI

Not Allowed

Report

↓

Generator

Audit

↓

Report

Power BI

↓

Generator

Any reverse dependency increases coupling and is prohibited.

---

# 16. COMMUNICATION RULES

Subsystems communicate only through well-defined objects.

Generator

↓

DataFrame

EDQE

↓

AuditSession

Report Builder

↓

Rendered Report

This minimizes coupling and allows future replacement of individual
components without affecting the rest of the system.

---

# 17. DATA CONTRACTS

Every subsystem exposes a stable contract.

Generator Output

pandas.DataFrame

EDQE Output

AuditSession

Report Output

HTML

Excel

Console

Future implementations must preserve these contracts unless a major
architecture revision is approved.

---
# ==========================================================
# 18. ARCHITECTURE FREEZE POLICY
# ==========================================================

Architecture Freeze is currently ACTIVE.

The current architecture has reached a level of stability suitable for
enterprise-scale development.

The purpose of Architecture Freeze is to protect the core framework from
unnecessary redesign while allowing new functionality to be added safely.

Protected Components

- AuditRunner
- AuditSession
- AuditResult
- AuditScore
- TABLE_RULES
- ReportBuilder Interface

These components shall only be modified when one of the following
conditions is satisfied.

1. A confirmed defect must be corrected.

2. A significant performance improvement is required.

3. A mandatory business requirement cannot be implemented through
   extension.

If none of the above conditions are met, proposed improvements shall be
recorded as "Improvement V2".

---

# 19. SINGLE SOURCE OF TRUTH (SSOT)

The project follows a strict Single Source of Truth policy.

Execution Result

AuditSession

Schema Metadata

TABLE_RULES

Business Rules

business/

Application Configuration

core/config.py

The same information must never be stored in multiple locations.

Duplicated metadata increases maintenance cost and introduces the risk of
inconsistent behavior.

Every subsystem must obtain information from its designated source.

---

# 20. DESIGN PATTERNS

The architecture intentionally uses lightweight design patterns.

----------------------------------------------------------

Pipeline Pattern

Generation

↓

Validation

↓

Audit

↓

Reporting

↓

Visualization

Each stage produces an output consumed by the next stage.

----------------------------------------------------------

Strategy Pattern

Each audit module implements a common execution contract.

Examples

MissingValueAudit

DuplicatePrimaryKeyAudit

ForeignKeyAudit

Future audit modules should follow the same strategy interface.

----------------------------------------------------------

Builder Pattern

ReportBuilder creates presentation output from AuditSession.

ConsoleReport

HTMLReport

ExcelReport

Each report builder is responsible only for rendering.

----------------------------------------------------------

Registry Pattern

TABLE_RULES acts as a centralized metadata registry.

Audit modules retrieve schema information from this registry instead of
embedding schema definitions inside audit logic.

----------------------------------------------------------

Facade Pattern

AuditRunner provides a single entry point for executing all audit
modules.

Client code should communicate with AuditRunner rather than individual
audit implementations.

---

# 21. MODULE INTERACTION

The interaction between core components follows a predictable sequence.

Generator

↓

DataFrame

↓

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

ReportBuilder

↓

Report Output

↓

Power BI

Each component has exactly one responsibility within this sequence.

---

# 22. EXTENSION POINTS

The framework has been designed for future extensibility.

Extension Point 1

New Audit Modules

A new audit can be introduced without modifying existing audit modules.

----------------------------------------------------------

Extension Point 2

New Report Formats

New report builders can be added without changing AuditRunner.

Examples

HTML

Excel

JSON

PDF

Markdown

----------------------------------------------------------

Extension Point 3

New Dataset Types

Future datasets may be added without changing the EDQE framework.

Examples

Fact_Inventory

Fact_Service

Fact_Return

Fact_Support

----------------------------------------------------------

Extension Point 4

Custom Validation Rules

Organization-specific validation rules may be added through new audit
modules rather than modifying the framework.

---

# 23. FUTURE PLUGIN ARCHITECTURE

Future versions will support a plugin system.

                      Plugin Loader
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Audit Plugin       Report Plugin      Export Plugin

The core framework should remain unchanged when plugins are installed.

Plugin responsibilities

Audit Plugin

- Custom validation

Report Plugin

- Custom reporting

Export Plugin

- Additional export formats

This design minimizes the need for core modifications.

---

# 24. PERFORMANCE CONSIDERATIONS

Performance is important but must not compromise architecture quality.

Current Priorities

1. Correctness

2. Maintainability

3. Readability

4. Extensibility

5. Performance

Potential future optimizations

- Parallel audit execution

- Incremental validation

- Cached metadata

- Lazy report generation

- Optimized DataFrame processing

Performance improvements should remain transparent to client code.

---

# 25. SECURITY CONSIDERATIONS

Although this project currently operates on locally generated datasets,
basic security principles are observed.

Configuration data should remain centralized.

Business rules should not be duplicated.

Generated reports should not expose internal implementation details.

Future versions should support:

- Configuration encryption

- Secure credentials

- Audit logging

- Access control

These features are outside the current project scope.

---

# 26. ERROR HANDLING PHILOSOPHY

Errors should be detected as early as possible.

Preferred order

Validate

↓

Audit

↓

Report

↓

Export

Every error should include sufficient information for debugging.

Silent failures are prohibited.

Unexpected exceptions should never be ignored.

---

# 27. TESTABILITY

The architecture is intentionally designed for testing.

Audit modules can be tested independently.

Generators can be tested independently.

Report builders can be tested independently.

Business rules can be tested independently.

Future testing layers

- Unit Testing

- Integration Testing

- Regression Testing

- Performance Testing

The modular architecture minimizes test complexity.

---

# 28. ARCHITECTURE DECISION RECORDS (ADR)

ADR-001

Adopt Enterprise Modular Architecture.

Status

Accepted

----------------------------------------------------------

ADR-002

Separate Data Generation from Data Validation.

Status

Accepted

----------------------------------------------------------

ADR-003

Introduce Enterprise Data Quality Engine.

Status

Accepted

----------------------------------------------------------

ADR-004

Adopt AuditSession as the execution result object.

Status

Accepted

----------------------------------------------------------

ADR-005

Use TABLE_RULES as metadata registry.

Status

Accepted

----------------------------------------------------------

ADR-006

Separate report generation from audit execution.

Status

Accepted

----------------------------------------------------------

ADR-007

Enable Architecture Freeze beginning with Sprint 18.3.2.

Status

Accepted

---

# ==========================================================
# 29. ARCHITECTURE QUALITY ATTRIBUTES
# ==========================================================

The architecture has been designed to satisfy the following quality
attributes.

----------------------------------------------------------

Maintainability

Priority

Very High

Objective

Allow future developers to understand and modify the system with minimal
effort.

Implementation

- Modular components
- Clear responsibilities
- Documentation-first development
- Architecture Freeze

----------------------------------------------------------

Scalability

Priority

High

Objective

Support future expansion without major redesign.

Examples

- Additional audit modules

- Additional report formats

- New fact tables

- New dimensions

- Plugin system

----------------------------------------------------------

Reliability

Priority

High

Objective

Produce consistent and repeatable audit results.

Implementation

- Deterministic processing

- Metadata-driven validation

- Standardized execution flow

----------------------------------------------------------

Extensibility

Priority

Very High

Objective

Support new functionality through extension rather than modification.

Implementation

- Modular audits

- Report builders

- Registry-based metadata

- Planned plugin architecture

----------------------------------------------------------

Readability

Priority

Very High

Objective

Ensure source code remains understandable.

Implementation

- Consistent naming

- Functional decomposition

- Complete documentation

- Black formatting

----------------------------------------------------------

Testability

Priority

High

Objective

Support independent testing for every subsystem.

Implementation

- Independent modules

- Stable contracts

- Predictable outputs

---

# 30. TECHNICAL DEBT POLICY

Technical debt should be minimized throughout development.

Acceptable technical debt

- Temporary implementation during active sprint

- Minor optimization opportunities

- Future plugin improvements

Unacceptable technical debt

- Duplicate business logic

- Hidden dependencies

- Circular references

- Architecture violations

- Inconsistent metadata

- Unreviewed refactoring

Whenever technical debt is intentionally accepted, it should be
documented as an Improvement V2 item.

---

# 31. DEPENDENCY MANAGEMENT

Dependencies should remain lightweight.

Current philosophy

Standard Library

+

Pandas

+

Power BI

Avoid unnecessary third-party packages.

Every dependency should satisfy at least one of the following.

- Improve maintainability

- Improve productivity

- Improve reliability

Dependencies should never be introduced solely for convenience.

---

# 32. CHANGE MANAGEMENT

Any architectural modification must follow this workflow.

Identify Requirement

↓

Architecture Review

↓

Impact Analysis

↓

Approval

↓

Implementation

↓

Testing

↓

Documentation Update

↓

Git Tag

Architecture modifications must never bypass documentation updates.

---

# 33. ARCHITECTURE REVIEW PROCESS

Architecture reviews should occur whenever one of the following happens.

- Completion of a major milestone

- Introduction of a new subsystem

- Framework redesign

- Significant performance issue

- New plugin capability

Review checklist

✓ Responsibilities remain clear

✓ No circular dependencies

✓ No duplicated logic

✓ Architecture Freeze respected

✓ SSOT respected

✓ Documentation synchronized

---

# 34. ARCHITECTURE COMPLIANCE CHECKLIST

Before completing any sprint, verify the following.

General

✓ Folder structure respected

✓ Naming conventions consistent

✓ Functional boundaries preserved

Architecture

✓ Architecture Freeze respected

✓ Single Source of Truth preserved

✓ Layer responsibilities maintained

✓ No prohibited dependencies

EDQE

✓ Audit modules remain independent

✓ AuditRunner responsibilities unchanged

✓ AuditSession remains execution result

Reporting

✓ Reports consume AuditSession only

✓ Reports contain no business logic

Documentation

✓ PROJECT_CONTEXT updated

✓ ROADMAP updated

✓ CHANGELOG updated

✓ MILESTONE_GIT updated

✓ AI documentation synchronized

---

# 35. FUTURE ARCHITECTURE VISION

The long-term vision extends beyond synthetic data generation.

Future enterprise capabilities may include

Data Layer

- SQL Server

- PostgreSQL

- MySQL

- Cloud Storage

Processing

- Batch Processing

- Streaming Validation

- Parallel Execution

Integration

- REST API

- Command Line Interface

- Python Package

Reporting

- Interactive HTML Reports

- PDF Reports

- Scheduled Reports

Deployment

- Docker

- CI/CD

- Cloud Deployment

- Automated Releases

The current architecture has been intentionally designed to accommodate
these future enhancements with minimal structural changes.

---

# 36. ARCHITECTURE GOVERNANCE

Architecture governance defines how architectural integrity is preserved.

Guiding Principles

- Prefer extension over modification.

- Protect core framework stability.

- Keep responsibilities isolated.

- Maintain complete documentation.

- Review before refactoring.

The project owner has final authority over architectural decisions.

AI assistants should recommend improvements but must not introduce
architectural changes without explicit approval.

---

# 37. DOCUMENT MAINTENANCE POLICY

This document shall be reviewed after:

- Major milestone completion

- Architecture modification

- New subsystem introduction

- Plugin framework implementation

Minor bug fixes do not require architecture updates.

Whenever this document changes, the following documentation should be
reviewed for consistency.

- PROJECT_CONTEXT.md

- ROADMAP.md

- CHANGELOG.md

- MILESTONE_GIT.md

- AI_DEVELOPMENT_RULES.md

- PROMPT_FOR_NEXT_SESSION.md

---

# 38. FINAL ARCHITECTURE SUMMARY

The Executive Marketing & Sales Dashboard project is based on an
enterprise modular architecture designed for long-term evolution.

Core architectural characteristics

✓ Enterprise Modular Design

✓ Functional Programming

✓ Layered Architecture

✓ Enterprise Data Quality Engine

✓ Metadata-Driven Validation

✓ Reporting Framework

✓ Architecture Freeze

✓ Single Source of Truth

✓ Documentation-First Development

✓ Git Milestone Strategy

✓ Future Plugin Architecture

The architecture emphasizes maintainability, extensibility, and
professional software engineering practices while remaining suitable as
a portfolio-quality project.

---

# ==========================================================
# END OF DOCUMENT
# ARCHITECTURE.md
# Version 1.0.0
# ==========================================================