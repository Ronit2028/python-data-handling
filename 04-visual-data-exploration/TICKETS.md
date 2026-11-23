# Sprint Tickets: Visual Data Exploration

**Assignee:** Arun Gupta  
**Reviewer / Instructor:** Ronit

---

## TL-VIZ-401: Histogram Binning & Skew Diagnostic
**Story Points:** 2 | **Timebox:** 15 mins | **File:** `starter_viz.py`

Implement `histogram_bins(values, num_bins=6)`:
- Return `num_bins` equal-width `(low, high, count)` tuples covering `min(values)..max(values)`.
- Verify total bin counts equal `len(values)`.

---

## TL-VIZ-402: Bar Chart Frequency Prep & Grouped Box Summary
**Story Points:** 3 | **Timebox:** 20 mins | **File:** `starter_viz.py`

Implement `bar_chart_counts(records, cat_col)` and `grouped_boxplot_stats(records, cat_col, num_col)`:
- For each category (e.g. `track`), compute `min`, `q1`, `median`, `q3`, `max` of `num_col` (`exam_score`).

---

## TL-VIZ-403: Diagnostic Scatter Plot SVG Renderer
**Story Points:** 5 | **Timebox:** 25 mins | **File:** `starter_viz.py`

Implement `render_scatter_svg(x, y, title, out_path)`:
- Render a clean 640x380 SVG scatter plot with `<circle>` markers for every `(study_hours, exam_score)` point and save to `out_path`.
