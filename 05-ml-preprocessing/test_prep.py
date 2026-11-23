"""Automated unit tests for TL-PRP-501, TL-PRP-502, and TL-PRP-503."""
import csv
import math
import os
import unittest
from pathlib import Path

if os.environ.get("USE_SOLUTIONS") == "1":
    import solutions as target
else:
    import starter_prep as target

DATA_PATH = Path(__file__).parent / "data" / "house_ml_prep.csv"


def _load():
    with open(DATA_PATH, mode="r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


class TestPreprocessing(unittest.TestCase):
    def test_01_leak_free_scaling(self):
        train = [10.0, 20.0, 30.0]
        test = [40.0]  # Must NOT affect train mean/std or min/max!
        mean, std = target.fit_standard_scaler(train)
        scaled_test = target.transform_standard_scaler(test, mean, std)
        self.assertAlmostEqual(mean, 20.0)
        self.assertGreater(scaled_test[0], 2.0)

        tr_mm, te_mm = target.minmax_scale(train, test)
        self.assertEqual(tr_mm, [0.0, 0.5, 1.0])
        self.assertEqual(te_mm, [1.5])  # > 1.0 proves test did not leak into fit!

    def test_02_categorical_encoding(self):
        ohe = target.one_hot_encode(["Bengaluru", "Mumbai", "Pune"], ["Bengaluru", "Mumbai", "Pune"])
        self.assertEqual(ohe, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

        ord_enc = target.ordinal_encode(["High", "Low", "Medium"], ["Low", "Medium", "High"])
        self.assertEqual(ord_enc, [2, 0, 1])

    def test_03_feature_engineering(self):
        rows = _load()
        enriched = target.engineer_features(rows)
        first = enriched[0]  # 2026-06-05 (Friday=4), area=1450, bedrooms=3, price=132.0
        self.assertEqual(first["list_month"], 6)
        self.assertEqual(first["list_dayofweek"], 4)
        self.assertAlmostEqual(first["sqft_per_bedroom"], 483.33, places=2)
        self.assertAlmostEqual(first["log_price"], round(math.log1p(132.0), 4), places=4)


if __name__ == "__main__":
    unittest.main()
