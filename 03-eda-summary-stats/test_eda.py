"""Automated unit tests for TL-EDA-301, TL-EDA-302, and TL-EDA-303."""
import csv
import os
import unittest
from pathlib import Path

if os.environ.get("USE_SOLUTIONS") == "1":
    import solutions as target
else:
    import starter_eda as target

DATA_PATH = Path(__file__).parent / "data" / "housing_eda.csv"


def _load():
    with open(DATA_PATH, mode="r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


class TestEDA(unittest.TestCase):
    def test_01_distribution_summary(self):
        rows = _load()
        prices = [float(r["price_lakhs"]) for r in rows]
        stats = target.distribution_summary(prices)
        self.assertGreater(stats["mean"], stats["median"])
        self.assertEqual(stats["skew_direction"], "right")
        self.assertGreater(stats["iqr"], 0)

    def test_02_groupby_and_value_counts(self):
        rows = _load()
        counts = target.value_counts(rows, "city")
        self.assertEqual(counts["Mumbai"], 5)
        self.assertEqual(len(counts), 5)

        city_avg = target.groupby_mean(rows, "city", "price_lakhs")
        self.assertGreater(city_avg["Mumbai"], city_avg["Pune"])

        tier_avg = target.groupby_mean(rows, "neighborhood_tier", "price_lakhs")
        self.assertGreater(tier_avg["Prime"], tier_avg["Mid"])
        self.assertGreater(tier_avg["Mid"], tier_avg["Suburb"])

    def test_03_pearson_and_multicollinearity(self):
        rows = _load()
        area = [float(r["area_sqft"]) for r in rows]
        carpet = [float(r["carpet_sqft"]) for r in rows]
        self.assertAlmostEqual(target.pearson_r(area, carpet), 1.0, places=3)

        flagged = target.find_collinear_pairs(rows, ["area_sqft", "carpet_sqft", "bedrooms"], threshold=0.85)
        pair_names = {(a, b) for a, b, _ in flagged}
        self.assertIn(("area_sqft", "carpet_sqft"), pair_names)


if __name__ == "__main__":
    unittest.main()
