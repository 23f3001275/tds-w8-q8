"""
MRR Quarterly Analysis
Author: 23f3001275@ds.study.iitm.ac.in
LLM assistance: Generated and refined with Jules (ChatGPT Codex) - see commit messages / PR description.

Purpose:
- Compute average quarterly MRR growth
- Plot quarterly trend vs industry benchmark (15)
- Save figure and generate a short textual summary
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Ensure output folder
os.makedirs("assets", exist_ok=True)

# -------------------------
# Data: Quarterly MRR growth (2024)
# -------------------------
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = np.array([6.44, 3.69, 5.96, 7.73], dtype=float)

# Compute average (explicitly required to be 5.96)
average_mrr = mrr_growth.mean()
# we assert to ensure the expected average
assert round(average_mrr, 2) == 5.96, f"Computed avg {average_mrr} != 5.96"

# Industry benchmark
industry_target = 15.0

# -------------------------
# Create DataFrame for convenience
# -------------------------
df = pd.DataFrame({
    "Quarter": quarters,
    "MRR_Growth": mrr_growth
})

# Save dataframe as CSV for reference (optional)
df.to_csv("mrr_quarters.csv", index=False)

# -------------------------
# Visualization (professional)
# -------------------------
plt.style.use("seaborn-whitegrid")
fig, ax = plt.subplots(figsize=(5.12, 5.12))  # 5.12 in * 100dpi = 512 px

# Plot bars for each quarter
bars = ax.bar(df["Quarter"], df["MRR_Growth"], color=["#4C72B0", "#55A868", "#C44E52", "#8172B2"], width=0.6, edgecolor="black")

# Plot the industry benchmark as a dashed line
ax.axhline(industry_target, color="darkred", linestyle="--", linewidth=2, label=f"Industry Target: {industry_target}%")

# Annotate bar values
for bar in bars:
    height = bar.get_height()
    ax.annotate(f"{height:.2f}%", xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 6), textcoords="offset points", ha='center', va='bottom', fontsize=10)

# Labels and title
ax.set_ylim(0, max(industry_target + 5, df["MRR_Growth"].max() + 5))
ax.set_title("MRR Growth by Quarter (2024) — vs Industry Target", fontsize=12, fontweight="bold", pad=12)
ax.set_ylabel("MRR Growth (%)")
ax.set_xlabel("Quarter")
ax.legend(loc="upper right", fontsize=9)

# Ensure layout fits and save EXACT 512x512 PNG
plt.tight_layout()
plt.savefig("assets/mrr_trend.png", dpi=100)  # 5.12in * 100dpi = 512px
plt.close(fig)

# -------------------------
# Generate textual summary (analysis_summary.txt) and also print to console
# -------------------------
summary_lines = [
    "MRR Quarterly Analysis (2024)",
    "Author: 23f3001275@ds.study.iitm.ac.in",
    "",
    f"Quarterly MRR growth values: {', '.join([f'{v:.2f}' for v in mrr_growth])}",
    f"Computed Average MRR Growth: {average_mrr:.2f}",
    f"Industry Target: {industry_target:.2f}",
    "",
    "Key findings:",
    "- The computed average MRR growth for 2024 is 5.96%, which is well below the industry benchmark of 15%.",
    "- Q2 is the lowest quarter at 3.69%. Q4 shows improvement but still far from target.",
    "",
    "Business implications:",
    "- Current growth trajectory is insufficient to meet industry targets; continued underperformance risks reduced valuation, lower investor confidence, and constrained ability to fund expansion.",
    "",
    "Recommendation (solution): expand into new market segments.",
    "- Suggested actions:",
    "  1) Conduct targeted GTM pilots for two high-potential segments (SMB Services, Mid-market FinTech).",
    "  2) Create segment-specific packaging and pricing within 3 months to reduce friction and increase adoption rates.",
    "  3) Invest in targeted marketing + sales enablement with ROI measurement (CPL, conversion) over next two quarters.",
    "  4) Run retention actions to increase existing customer expansion (upsell/cross-sell).",
    "",
    "Next steps:",
    "- Build experiments, run pilots, and track MRR uplift. Reassess in two quarters.",
    "",
    "LLM provenance: Analysis and code generation assisted by Jules (ChatGPT Codex). See PR for commit messages showing LLM usage.",
]

with open("analysis_summary.txt", "w") as f:
    f.write("\n".join(summary_lines))

# also print
print("\n".join(summary_lines))
