"""Automated unit tests for TL-DATA-101, TL-DATA-102, and TL-DATA-103."""
import os
import unittest
from pathlib import Path

# Set USE_SOLUTIONS=1 to verify reference solutions
if os.environ.get("USE_SOLUTIONS") == "1":
    import solutions as target
else:
    import starter_assignment as target

DATA_DIR = Path(__file__).parent / "data"


class TestDataLoadingAndInspection(unittest.TestCase):
    def test_01_load_csv_json_excel(self):
        props = target.load_csv_records(DATA_DIR / "properties.csv")
        agents = target.load_json_records(DATA_DIR / "agents.json")
        sales = target.load_excel_sheet(DATA_DIR / "sales_records.xlsx", sheet_name="Q4_Sales")

        self.assertEqual(len(props), 20)
        self.assertEqual(len(props[0]), 10)
        self.assertEqual(len(agents), 5)
        self.assertEqual(agents[0]["agent_id"], "AG-01")
        self.assertEqual(len(sales), 10)
        self.assertEqual(sales[0]["sale_id"], "SAL-501")

    def test_02_sanity_audit(self):
        props = target.load_csv_records(DATA_DIR / "properties.csv")
        audit = target.sanity_audit(props)

        self.assertEqual(audit["shape"], (20, 10))
        self.assertEqual(audit["missing_counts"]["area_sqft"], 1)
        self.assertEqual(audit["missing_counts"]["age_years"], 1)
        self.assertEqual(audit["missing_counts"]["city"], 0)
        self.assertEqual(audit["nunique"]["city"], 5)
        self.assertEqual(audit["nunique"]["condition"], 4)
        self.assertIn("property_id", audit["id_like_columns"])
        self.assertIn("agent_notes", audit["id_like_columns"])

    def test_03_column_classification_and_ml_gate(self):
        props = target.load_csv_records(DATA_DIR / "properties.csv")
        cols = list(props[0].keys())

        self.assertEqual(target.classify_column_role("area_sqft"), "continuous")
        self.assertEqual(target.classify_column_role("bedrooms"), "discrete")
        self.assertEqual(target.classify_column_role("city"), "nominal")
        self.assertEqual(target.classify_column_role("condition"), "ordinal")
        self.assertEqual(target.classify_column_role("listing_date"), "datetime")
        self.assertEqual(target.classify_column_role("property_id"), "id")
        self.assertEqual(target.classify_column_role("agent_notes"), "text")

        features, dropped, y = target.prepare_ml_columns(cols, target_col="price_lakhs")
        self.assertEqual(y, "price_lakhs")
        self.assertEqual(set(dropped), {"property_id", "agent_id", "agent_notes", "listing_date"})
        self.assertEqual(set(features), {"city", "condition", "area_sqft", "bedrooms", "age_years"})


if __name__ == "__main__":
    unittest.main()
