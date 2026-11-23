"""
TechLearns AI/ML — Visual Data Exploration (Diagnostic Plots)
Instructor: Ronit | Student: Arun Gupta

Run in an environment with pandas, matplotlib & seaborn installed:
    python3 code_samples.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(Path(__file__).parent / "data" / "student_performance_viz.csv")

# Focus on diagnostic plots rather than heavy styling
fig, axes = plt.subplots(2, 3, figsize=(14, 8))

# 1. Single-variable: Histogram (check shape & skewness)
sns.histplot(df["practice_problems"], bins=6, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Histogram: practice_problems (Skew)")

# 2. Single-variable: Box plot (spot outliers & IQR)
sns.boxplot(x=df["exam_score"], ax=axes[0, 1])
axes[0, 1].set_title("Box Plot: exam_score")

# 3. Single-variable: Bar chart (category counts)
sns.countplot(x="track", data=df, ax=axes[0, 2])
axes[0, 2].set_title("Bar Chart: track counts")

# 4. Two-variable: Scatter plot (numeric vs. numeric)
sns.scatterplot(x="study_hours", y="exam_score", hue="track", data=df, ax=axes[1, 0])
axes[1, 0].set_title("Scatter: study_hours vs. exam_score")

# 5. Two-variable: Grouped box plot (categorical vs. numeric)
sns.boxplot(x="track", y="exam_score", data=df, ax=axes[1, 1])
axes[1, 1].set_title("Grouped Box Plot: track vs. exam_score")

axes[1, 2].axis("off")
plt.tight_layout()
plt.savefig("diagnostic_eda_grid.png", dpi=150)
print("Saved diagnostic_eda_grid.png")
