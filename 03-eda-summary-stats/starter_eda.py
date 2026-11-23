"""
Starter Assignment: Exploratory Data Analysis & Summary Stats
Assignee: Arun Gupta | Reviewer: Ronit
"""


# TL-EDA-301
def distribution_summary(values: list[float]) -> dict:
    """Return mean, median, std (ddof=1), q1, q3, iqr, and skew_direction."""
    raise NotImplementedError("Complete TL-EDA-301: distribution_summary")


# TL-EDA-302
def value_counts(records: list[dict], col: str) -> dict[str, int]:
    """Return frequency count of each distinct value in `col`."""
    raise NotImplementedError("Complete TL-EDA-302: value_counts")


def groupby_mean(records: list[dict], group_col: str, target_col: str) -> dict[str, float]:
    """Return {group: round(mean(target_col), 2)} for each group."""
    raise NotImplementedError("Complete TL-EDA-302: groupby_mean")


# TL-EDA-303
def pearson_r(x: list[float], y: list[float]) -> float:
    """Compute Pearson correlation coefficient r rounded to 4 decimals."""
    raise NotImplementedError("Complete TL-EDA-303: pearson_r")


def find_collinear_pairs(records: list[dict], numeric_cols: list[str], threshold: float = 0.85) -> list[tuple[str, str, float]]:
    """Return list of (col_a, col_b, r) where |r| >= threshold."""
    raise NotImplementedError("Complete TL-EDA-303: find_collinear_pairs")
