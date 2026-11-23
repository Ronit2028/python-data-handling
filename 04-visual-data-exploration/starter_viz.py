"""
Starter Assignment: Visual Data Exploration
Assignee: Arun Gupta | Reviewer: Ronit
"""
from pathlib import Path


# TL-VIZ-401
def histogram_bins(values: list[float], num_bins: int = 6) -> list[tuple[float, float, int]]:
    """Return list of (low, high, count) tuples for equal-width histogram bins."""
    raise NotImplementedError("Complete TL-VIZ-401: histogram_bins")


# TL-VIZ-402
def bar_chart_counts(records: list[dict], cat_col: str) -> dict[str, int]:
    """Return category frequency counts for a bar chart."""
    raise NotImplementedError("Complete TL-VIZ-402: bar_chart_counts")


def grouped_boxplot_stats(records: list[dict], cat_col: str, num_col: str) -> dict[str, dict]:
    """Return {category: {'min', 'q1', 'median', 'q3', 'max'}} for grouped box plots."""
    raise NotImplementedError("Complete TL-VIZ-402: grouped_boxplot_stats")


# TL-VIZ-403
def render_scatter_svg(x: list[float], y: list[float], title: str, out_path: Path) -> Path:
    """Render a 640x380 SVG scatter plot of (x, y) points and write to out_path."""
    raise NotImplementedError("Complete TL-VIZ-403: render_scatter_svg")
