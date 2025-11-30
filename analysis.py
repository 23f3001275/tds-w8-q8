"""
MRR Quarterly Analysis
Author: 23f3001275@ds.study.iitm.ac.in
LLM assistance: Generated and refined with Jules (ChatGPT Codex)

Produces:
- assets/mrr_trend.png  (512x512)
- mrr_quarters.csv
- analysis_summary.txt
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("assets", exist_ok=True)

# Data
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = np.array([6.44, 3.69, 5.96, 7.73], dtype=float)
average_mrr = mrr_growth.mean()
assert round(average_mrr, 2) == 5.96, f"Average mismatch: {average_mrr}"

industry_target = 15.0

# Save CSV
df = pd.DataFrame({"Quarter": quarters, "MRR_Growth": mrr_growth})
df.to_csv("mrr_quarters.csv", index=False)

# Plot
sns.set_style("whitegrid")
sns.set_context("talk")
fig, ax = plt.subplots(figsize=(5.12, 5.12))  # 5.12 in * 100 dpi = 512 px

colors = ["#4C72B0", "#55A868", "#C44E52", "#8172B2"]
bars = ax.bar(df["Quarter"], df["MRR_Growth"], color=colors, edgecolor="black", width=0.6)

ax.axhline(industry_target, color="darkred", linestyle="--", linewidth=2, label=f"Industry Target: {industry_target}%")

for bar in bars:
    h = bar.get_height()
    ax.annotate(f"{h:.2f}%", xy=(bar.get_x() + bar.get_width()/2, h),
                xytext=(0, 6), textcoords="offset points", ha="center", va="bottom", fontsize=10)

ax.set_ylim(0, max(industry_target + 5, df["MRR_Growth"].max() + 5))
ax.set_title("MRR Growth by Quarter (2024) — vs Industry Target", fontsize=14, fontweight="bold", pad=12)
ax.set_xlabel("Quarter")
ax.set_ylabel("MRR Growth (%)")
ax.legend(loc="upper right", fontsize=9)

plt.tight_layout()
plt.savefig("assets/mrr_trend.png", dpi=100)  # 5.12 * 100 = 512 px
plt.close(fig)

# Summary file
summary = f"""MRR Quarterly Analysis (2024)
Author: 23f3001275@ds.study.iitm.ac.in

Quarterly MRR growth values: {', '.join([f'{v:.2f}' for v in mrr_growth])}
Computed Average MRR Growth: {average_mrr:.2f}
Industry Target: {industry_target:.2f}

Key findings:
- The computed average MRR growth for 2024 is 5.96%, which is well below the industry benchmark of 15%.
- Q2 is the lowest quarter at 3.69%. Q4 shows improvement but still far from target.

Recommendation (solution): expand into new market segments.
"""

with open("analysis_summary.txt", "w") as f:
    f.write(summary)
