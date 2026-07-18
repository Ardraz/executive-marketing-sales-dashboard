"""
Enterprise Data Quality Engine (EDQE)

Reusable HTML Components
"""

from __future__ import annotations

from html import escape

# ============================================================
# Utilities
# ============================================================


def _escape(value) -> str:
    """HTML escape helper."""
    return escape(str(value))


# ============================================================
# Header
# ============================================================


def render_header(
    project: str,
    engine: str,
    version: str,
) -> str:

    return f"""
<header class="header">
    <h1>{_escape(project)}</h1>
    <div class="subtitle">{_escape(engine)}</div>
    <div class="version">
        Version {version}
    </div>
</header>
"""


# ============================================================
# KPI Card
# ============================================================


def render_kpi_card(
    title: str,
    value,
    color: str = "primary",
    icon: str = "",
) -> str:

    return f"""
<div class="kpi-card {color}">
    <div class="kpi-icon">
        {icon}
    </div>

    <div class="kpi-title">
        {_escape(title)}
    </div>

    <div class="kpi-value">
        {_escape(value)}
    </div>
</div>
"""


# ============================================================
# Section Title
# ============================================================


def render_section_title(
    title: str,
) -> str:

    return f"""
<h2 class="section-title">
    {_escape(title)}
</h2>
"""


# ============================================================
# Information Table
# ============================================================


def render_info_table(
    rows: list[tuple[str, str]],
) -> str:

    body = ""

    for key, value in rows:

        body += f"""
<tr>
    <th>{_escape(key)}</th>
    <td>{_escape(value)}</td>
</tr>
"""

    return f"""
<table class="info-table">
<tbody>

{body}

</tbody>
</table>
"""


# ============================================================
# Status Badge
# ============================================================


def render_badge(
    status: str,
) -> str:

    value = status.upper()

    color = "secondary"

    if value == "PASS":
        color = "success"

    elif value == "FAILED":
        color = "danger"

    elif value == "WARNING":
        color = "warning"

    return f'<span class="badge badge-{color}">' f"{_escape(value)}" "</span>"


# ============================================================
# DataFrame Summary
# ============================================================


def render_dataframe_table(
    dataframe_summary: dict,
) -> str:

    rows = ""

    for table, info in dataframe_summary.items():

        rows += f"""
<tr>

<td>{_escape(table)}</td>

<td>{info["rows"]:,}</td>

<td>{info["columns"]}</td>

<td>{info["memory_mb"]:.2f} MB</td>

</tr>
"""

    return f"""
<table class="table">

<thead>

<tr>

<th>Table</th>

<th>Rows</th>

<th>Columns</th>

<th>Memory</th>

</tr>

</thead>

<tbody>

{rows}

</tbody>

</table>
"""


# ============================================================
# Audit Result Table
# ============================================================


def render_audit_table(
    results,
) -> str:

    rows = ""

    for result in results:

        status = "PASS" if result.passed else "FAILED"

        rows += f"""
<tr>

<td>{_escape(result.name)}</td>

<td>{render_badge(status)}</td>

<td>{result.error_count}</td>

<td>{result.warning_count}</td>

<td>{_escape(result.description)}</td>

</tr>
"""

    return f"""
<table class="table">

<thead>

<tr>

<th>Audit</th>

<th>Status</th>

<th>Errors</th>

<th>Warnings</th>

<th>Description</th>

</tr>

</thead>

<tbody>

{rows}

</tbody>

</table>
"""


# ============================================================
# Recommendation Panel
# ============================================================


def render_recommendation(
    recommendation,
) -> str:

    return f"""
<div class="recommendation {recommendation.color}">

<h2>

{_escape(recommendation.title)}

</h2>

<p>

{_escape(recommendation.summary)}

</p>

<h4>

Recommended Action

</h4>

<p>

{_escape(recommendation.action)}

</p>

</div>
"""


# ============================================================
# Footer
# ============================================================


def render_footer() -> str:

    return """
<footer class="footer">

Generated automatically by

Enterprise Data Quality Engine

</footer>
"""
