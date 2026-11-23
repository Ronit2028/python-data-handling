"""
Starter Assignment: ML Preprocessing (The Bridge from Data to ML)
Assignee: Arun Gupta | Reviewer: Ronit
"""


# TL-PRP-501
def fit_standard_scaler(train_vals: list[float]) -> tuple[float, float]:
    """Return (mean, std) computed ONLY on training data."""
    raise NotImplementedError("Complete TL-PRP-501: fit_standard_scaler")


def transform_standard_scaler(vals: list[float], mean: float, std: float) -> list[float]:
    """Scale values using pre-fit (mean, std) from training data."""
    raise NotImplementedError("Complete TL-PRP-501: transform_standard_scaler")


def minmax_scale(train_vals: list[float], test_vals: list[float]) -> tuple[list[float], list[float]]:
    """Fit min/max on train_vals only, then scale both train_vals and test_vals."""
    raise NotImplementedError("Complete TL-PRP-501: minmax_scale")


# TL-PRP-502
def one_hot_encode(values: list[str], categories: list[str]) -> list[list[int]]:
    """Convert nominal category list into 0/1 one-hot vectors."""
    raise NotImplementedError("Complete TL-PRP-502: one_hot_encode")


def ordinal_encode(values: list[str], ordered_levels: list[str]) -> list[int]:
    """Convert ordered category list into 0..K-1 integers."""
    raise NotImplementedError("Complete TL-PRP-502: ordinal_encode")


# TL-PRP-503
def engineer_features(records: list[dict]) -> list[dict]:
    """
    Add 'list_month', 'list_dayofweek', 'sqft_per_bedroom', and 'log_price'
    to each property record dict.
    """
    raise NotImplementedError("Complete TL-PRP-503: engineer_features")
