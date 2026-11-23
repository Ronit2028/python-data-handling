"""Automated unit tests for TL-VIZ-401, TL-VIZ-402, and TL-VIZ-403."""
import csv
import os
import tempfile
import unittest
from pathlib import Path

if os.environ.get("USE_SOLUTIONS") == "1":
    import solutions as target
else:
    import starter_viz as target

DATA_PATH = Path(__file__).parent / "data" / "student_performance_viz.csv"


def _load():
    with open(DATA_PATH, mode="r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


class TestVisualEDA(unittest.TestCase):
    def test_01_histogram_bins(self):
        rows = _load()
        probs = [float(r["practice_problems"]) for r in rows]
        bins = target.histogram_bins(probs, num_bins=6)
        self.assertEqual(len(bins), 6)
        self.assertEqual(sum(b[2] for b in bins), len(rows))

    def test_02_bar_and_grouped_boxplot(self):
        rows = _load()
        counts = target.bar_chart_counts(rows, "track")
        self.assertEqual(counts, {"AI/ML": 8, "Data Eng": 8, "Web Dev": 8})

        box = target.grouped_boxplot_stats(rows, "track", "exam_score")
        self.assertGreater(box["AI/ML"]["median"], box["Web Dev"]["median"])

    def test_03_render_scatter_svg(self):
        rows = _load()
        x = [float(r["study_hours"]) for r in rows]
        y = [float(r["exam_score"]) for r in rows]
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "scatter.svg"
            target.render_scatter_svg(x, y, "Study Hours vs Exam Score", out)
            content = out.read_text(encoding="utf-8")
            self.assertIn("<svg", content)
            self.assertEqual(content.count("<circle"), 24)


if __name__ == "__main__":
    unittest.main()
