"""
Starter Assignment: Data Loading & First-Look Inspection
Assignee: Arun Gupta | Reviewer: Ronit

Complete the functions below to solve TL-DATA-101, TL-DATA-102, and TL-DATA-103.
Run tests with:
    python3 -m unittest -v test_assignment.py
"""
import csv
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


# ----------------------------------------------------------------------------
# TL-DATA-101: Multi-Format Ingestion (CSV, JSON, Excel)
# ----------------------------------------------------------------------------
def load_csv_records(path: Path) -> list[dict]:
    """Read a CSV file and return a list of row dicts."""
    raise NotImplementedError("Complete TL-DATA-101: load_csv_records")


def load_json_records(path: Path) -> list[dict]:
    """Read a JSON array-of-objects file and return a list of dicts."""
    raise NotImplementedError("Complete TL-DATA-101: load_json_records")


def load_excel_sheet(path: Path, sheet_name: str = "Q4_Sales") -> list[dict]:
    """Read a named worksheet from an .xlsx file and return a list of row dicts."""
    raise NotImplementedError("Complete TL-DATA-101: load_excel_sheet")


# ----------------------------------------------------------------------------
# TL-DATA-102: First-Look Sanity Audit
# ----------------------------------------------------------------------------
def sanity_audit(records: list[dict]) -> dict:
    """
    Inspect loaded records and return a dict with:
      - 'shape': (num_rows, num_cols)
      - 'missing_counts': {col: count of None or ''}
      - 'nunique': {col: count of distinct non-empty values}
      - 'id_like_columns': [cols where nunique == num_rows]
    """
    raise NotImplementedError("Complete TL-DATA-102: sanity_audit")


# ----------------------------------------------------------------------------
# TL-DATA-103: Column Type Classifier & ML Readiness Gate
# ----------------------------------------------------------------------------
VALID_ROLES = {"continuous", "discrete", "nominal", "ordinal", "datetime", "id", "text"}


def classify_column_role(col_name: str) -> str:
    """
    Map a column from properties.csv to one of VALID_ROLES:
    'continuous', 'discrete', 'nominal', 'ordinal', 'datetime', 'id', or 'text'.
    """
    raise NotImplementedError("Complete TL-DATA-103: classify_column_role")


def prepare_ml_columns(columns: list[str], target_col: str = "price_lakhs") -> tuple[list[str], list[str], str]:
    """
    Split columns into (feature_cols, dropped_cols, target_col).
    Drop 'id', 'text', and raw 'datetime' columns so ML models don't ingest them directly.
    """
    raise NotImplementedError("Complete TL-DATA-103: prepare_ml_columns")
