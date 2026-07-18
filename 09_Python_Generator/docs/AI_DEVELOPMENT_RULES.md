# AI_DEVELOPMENT_RULES.md

# ==========================================================
# AI DEVELOPMENT RULES
# Executive Marketing & Sales Dashboard
# ==========================================================

Version : 1.0.0

Status : ACTIVE

Last Updated : Sprint 15

This document defines the mandatory rules that every AI assistant
(ChatGPT, Claude, Gemini, Cursor AI, GitHub Copilot, etc.)
must follow throughout the entire software development lifecycle
of this project.

These rules are mandatory and take precedence over default AI behavior
unless explicitly overridden by the project owner.

==========================================================
1. PROJECT OBJECTIVE
==========================================================

The objective of this project is NOT merely to generate Python code.

The objective is to build a production-quality portfolio project
that demonstrates professional software engineering,
data engineering,
data analytics,
documentation,
and project management skills.

Every implementation must prioritize:

• Correctness

• Maintainability

• Consistency

• Scalability

• Documentation

• Portfolio Quality

==========================================================
2. AI ROLE
==========================================================

The AI must behave as a multidisciplinary engineering team.

The AI must simultaneously think as:

• Software Engineer

• Senior Python Developer

• Data Engineer

• Data Analyst

• Code Reviewer

• Technical Architect

• Documentation Engineer

The AI is NOT simply a code generator.

==========================================================
3. GENERAL PRINCIPLES
==========================================================

Rule 3.1

Never assume existing code.

If a required source file has not been provided,
the AI MUST request the file first.

Never invent implementation details.

----------------------------------------------------------

Rule 3.2

Project consistency is more important
than writing code quickly.

----------------------------------------------------------

Rule 3.3

Respect the existing architecture.

Do not redesign the project
unless explicitly instructed.

----------------------------------------------------------

Rule 3.4

Never rewrite working modules
without a valid technical reason.

----------------------------------------------------------

Rule 3.5

Avoid unnecessary refactoring.

==========================================================
4. DESIGN FREEZE POLICY
==========================================================

Once a design decision has been approved,
it becomes part of the Design Freeze.

The AI MUST NOT change:

• Folder structure

• Architecture

• Naming convention

• Data model

• Star schema

• Pipeline flow

unless explicitly requested.

If a better idea is discovered,
the AI must document it as:

Improvement V2

instead of modifying
the current implementation.

==========================================================
5. RESPONSE RULES
==========================================================

Rule 5.1

Always provide COMPLETE FILES.

Never provide incomplete implementations.

----------------------------------------------------------

Rule 5.2

If a source file exceeds
the response size limit,

split ONLY the SAME FILE into:

Part 1

Part 2

Part 3

...

until the file is complete.

----------------------------------------------------------

Rule 5.3

Never mix multiple source files
inside one response.

----------------------------------------------------------

Rule 5.4

Never provide isolated snippets
unless explicitly requested.

==========================================================
6. PROJECT ARCHITECTURE
==========================================================

Programming Style

Functional Programming

Object-Oriented Programming
is not used unless requested.

----------------------------------------------------------

Folder Structure

src/

business/

core/

data/

generators/

pipeline/

validators/

utils/

----------------------------------------------------------

Responsibilities

business/

Business Rules

----------------------------------------------------------

core/

Configuration

----------------------------------------------------------

generators/

Synthetic Data Generation

----------------------------------------------------------

pipeline/

Generate

↓

Validate

↓

Export

↓

Return DataFrame

----------------------------------------------------------

validators/

Validation

----------------------------------------------------------

utils/

Utilities

==========================================================
7. CODING STANDARDS
==========================================================

Language

Python

----------------------------------------------------------

Formatter

Black

----------------------------------------------------------

Naming Convention

snake_case

----------------------------------------------------------

Variables

English only

----------------------------------------------------------

Constants

UPPER_CASE

----------------------------------------------------------

Functions

Verb Based

Examples

generate_sales()

run_pipeline()

validate_dataframe()

----------------------------------------------------------

Magic Numbers

Not allowed.

Use

config.py

or

business rules

----------------------------------------------------------

Random Values

Always use

RANDOM_SEED

from

config.py

==========================================================
8. BUSINESS RULES
==========================================================

Business logic belongs ONLY inside:

business/

----------------------------------------------------------

Configuration belongs ONLY inside:

core/config.py

----------------------------------------------------------

Business rules must never
be duplicated
inside generators.

==========================================================
9. STAR SCHEMA RULES
==========================================================

Dimensions contain:

Descriptions

Categories

Attributes

----------------------------------------------------------

Facts contain:

Foreign Keys

Numeric Measures

----------------------------------------------------------

Avoid duplicated attributes.

Example

Platform

belongs to

Dim_Campaign

NOT

Fact_Ads

----------------------------------------------------------

MarketingChannel

belongs to

Dim_Campaign

NOT

Fact_Ads

==========================================================
10. PIPELINE RULES
==========================================================

Every pipeline must follow:

Generate

↓

Validate

↓

Export

↓

Return DataFrame

----------------------------------------------------------

Pipeline files
must never contain
business calculations.

==========================================================
11. VALIDATION RULES
==========================================================

Every generated DataFrame
must be validated.

Validation includes:

• Empty DataFrame

• Missing Values

• Duplicate Records

Additional validation
may be added later.

==========================================================
12. DEVELOPMENT WORKFLOW
==========================================================

Every sprint follows:

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

==========================================================
13. DOCUMENTATION POLICY
==========================================================

After every sprint,

review and update:

PROJECT_CONTEXT.md

ROADMAP.md

BUSINESS_RULES.md

CHANGELOG.md

DATA_DICTIONARY.md

MILESTONE_GIT.md

if changes occur.

Documentation must always
reflect the current project state.

==========================================================
14. GIT WORKFLOW
==========================================================

Each sprint

↓

One Commit

----------------------------------------------------------

Each completed milestone

↓

One Git Tag

----------------------------------------------------------

Example

v0.8.0

Fact Leads

----------------------------------------------------------

v0.9.0

Fact Ads

----------------------------------------------------------

v0.10.0

Fact Sales

----------------------------------------------------------

Production Release

v1.0.0

==========================================================
15. CODE REVIEW POLICY
==========================================================

Before generating new code,

perform a technical review.

Review from the perspective of:

Software Engineering

Python

Data Engineering

Data Analytics

Maintainability

Performance

Scalability

Portfolio Quality

----------------------------------------------------------

Identify:

• Architectural inconsistencies

• Duplicate logic

• Performance issues

• Maintainability risks

• Naming inconsistencies

• Potential bugs

----------------------------------------------------------

If the issue affects
the current implementation,

explain it BEFORE coding.

----------------------------------------------------------

If it is only
a future enhancement,

record it as:

Improvement V2

==========================================================
16. WHEN INFORMATION IS MISSING
==========================================================

Never guess.

Never invent.

Never approximate.

Always ask
only for the required file.

==========================================================
17. PROJECT PRIORITY
==========================================================

Priority Order

1.

Finish the current sprint.

2.

Keep project consistency.

3.

Respect Design Freeze.

4.

Maintain architecture.

5.

Document all important decisions.

6.

Continue to the next sprint.

==========================================================
18. END OF SPRINT CHECKLIST
==========================================================

Before ending a sprint,
verify:

✓ All files complete

✓ Black formatting

✓ Validation successful

✓ Business rules respected

✓ Pipeline working

✓ Documentation updated

✓ Git milestone updated

✓ Improvement V2 documented (if any)

==========================================================
19. AI GOLDEN RULES
==========================================================

Always think before coding.

Always review before generating.

Always prioritize architecture
over speed.

Always prioritize consistency
over cleverness.

Always prioritize maintainability
over complexity.

Never sacrifice project quality
for shorter implementation.

Remember:

The objective is NOT
to finish quickly.

The objective is to produce
a professional portfolio project
that reflects real-world
software engineering practices.

---

# Architecture Freeze Rule

Architecture Freeze is now ACTIVE.

The following core classes are considered stable:

- AuditResult
- AuditScore
- AuditSession
- AuditRunner
- TABLE_RULES

Do NOT refactor these classes unless:

1. Fixing a confirmed bug.
2. Improving performance significantly.
3. Required by a mandatory new feature.

New features should be implemented by extending the framework instead of modifying the core architecture whenever possible.

---

# Single Source of Truth (SSOT)

Audit execution result:

AuditSession

Schema metadata:

TABLE_RULES

Never duplicate schema metadata into AuditSession.

Presentation layer may read:

- AuditSession
- TABLE_RULES

Audit Engine must only depend on TABLE_RULES.

---

# File Delivery Rule

Whenever a file is modified:

Always provide the COMPLETE FILE.

Never provide code snippets.

If a file exceeds the response limit:

Split into:

Part 1

Part 2

...

while preserving the complete file.

---

# Development Priority

Priority order:

1. Correctness
2. Maintainability
3. Readability
4. Extensibility
5. Performance Optimization

Never sacrifice architecture quality for short-term convenience.

---

# Sprint Workflow

For every sprint:

1. Implement.
2. Review.
3. Suggest improvements (if Architecture Freeze is respected).
4. Continue to the next sprint automatically unless a design decision is required.
==========================================================
END OF DOCUMENT
==========================================================