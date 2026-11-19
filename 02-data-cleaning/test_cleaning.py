"""Automated unit tests for TL-CLN-201, TL-CLN-202, and TL-CLN-203."""
import csv
import os
import unittest
from pathlib import Path

if os.environ.get("USE_SOLUTIONS") == "1":
    import solutions as target
else:
    import starter_cleaning as target

DATA_PATH = Path(__file__).parent / "data" / "messy_housing_deals.csv"


def _load_raw():
    with open(DATA_PATH, mode="r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


class TestDataCleaning(unittest.TestCase):
    def test_01_missing_audit_and_imputation(self):
        rows = _load_raw()
        missing = target.count_missing(rows)
        self.assertEqual(missing["city"], 1)
        self.assertEqual(missing["condition"], 1)
        self.assertEqual(missing["area_sqft"], 1)
        self.assertEqual(missing["bedrooms"], 1)

        imputed_num = target.impute_missing_numeric([1000, 1320, 9999, None], strategy="median")
        self.assertEqual(imputed_num, [1000.0, 1320.0, 9999.0, 1320.0])

        imputed_cat = target.impute_missing_category(["Pune", "Mumbai", "Pune", ""])
        self.assertEqual(imputed_cat[-1], "Pune")

        imputed_const = target.impute_missing_category(["Good", None], constant="Unknown")
        self.assertEqual(imputed_const[-1], "Unknown")

    def test_02_dedup_and_formatting(self):
        rows = _load_raw()
        self.assertEqual(len(rows), 22)
        deduped = target.deduplicate_rows(rows)
        self.assertEqual(len(deduped), 20)

        self.assertEqual(target.clean_category(" mumbai "), "Mumbai")
        self.assertEqual(target.clean_category("EXCELLENT"), "Excellent")
        self.assertIsNone(target.clean_category(""))

        self.assertEqual(target.parse_messy_number("$1,200"), 1200.0)
        self.assertEqual(target.parse_messy_number("1,450"), 1450.0)
        self.assertEqual(target.parse_messy_number("980 sqft"), 980.0)
        self.assertIsNone(target.parse_messy_number("N/A"))

    def test_03_iqr_outliers_and_regression_tilt(self):
        rows = target.deduplicate_rows(_load_raw())
        areas = target.impute_missing_numeric(
            [target.parse_messy_number(r["area_sqft"]) for r in rows],
            strategy="median",
        )
        prices = [float(r["price_lakhs"]) for r in rows]

        res = target.iqr_outliers(prices)
        self.assertIn(999.0, res["outliers"])

        slope_with = target.ols_slope(areas, prices)
        clean_pairs = [(a, p) for a, p in zip(areas, prices) if p <= res["upper_fence"]]
        slope_without = target.ols_slope(
            [a for a, _ in clean_pairs],
            [p for _, p in clean_pairs],
        )
        # The 999.0 outlier at area=1040 pulls the slope sharply down/flat compared to clean data
        self.assertNotEqual(slope_with, slope_without)
        self.assertGreater(slope_without, slope_with)


if __name__ == "__main__":
    unittest.main()
