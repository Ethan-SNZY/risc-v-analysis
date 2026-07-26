import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Loading data
df = pd.read_csv("data/stars_and_commits.csv")

#Graph Style
plt.style.use('seaborn-v0_8-whitegrid')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14,6))

#Readability adjustments

df["short_name"] = df["repo"].str.replace("riscv/","")\
                                           .str.replace("lowRISC/","")\
                                           .str.replace("chipsalliance/","")\
                                           .str.replace("ARM-software/","")\
                                           .str.replace("riscv-software-src/","")

#Stars Chart
bars1 = ax1.barh(df["short_name"], df["stars"], color="#2563eb", alpha=0.85,edgecolor="white")

for bar in bars1:
    width = bar.get_width()
    ax1.text(width + 30, bar.get_y() + bar.get_height()/2, f"{int(width):,}", va="center", fontsize=9, color="grey")


    ax1.set_xlabel("Total Github Stars", fontsize=10)
    ax1.set_title("GitHub Stars\n(Community Interest)", fontsize=11, fontweight="bold")
    ax1.set_xlim(0, df["stars"].max() * 1.2)

#Commits Chart
bars2 = ax2.barh(df["short_name"], df["recent_commits"], color="#DC2626", alpha=0.85, edgecolor="white")

for bar in bars2:
    width = bar.get_width()
    ax2.text(width + 0.3, bar.get_y() + bar.get_height()/2, str(int(width)), va="center", fontsize=9, color="grey")

    ax2.set_xlabel("Github Commits in past 30 days", fontsize=10)
    ax2.set_title("GitHub Commits\n(Development Activity)", fontsize=11, fontweight="bold")
    ax2.set_xlim(0, df["recent_commits"].max() * 1.3)

    ax2.tick_params(axis='x')
    ax2.set_ylabel("Repository", fontsize=10)

#Titles and Labels
fig.suptitle("RISC-V Repository Snapshot: Spec vs Implementation\n" \
"riscv-isa-manual & lowRISC/ibex", fontsize=14, fontweight="bold", y=1.05)

#Source Note
fig.text(0.5, -0.05, "Source: GitHub API · Stars = community interest · Commits = development activity", ha="right", fontsize=7.5, color="grey")

plt.tight_layout()
plt.savefig("data/github_chart.png", dpi=150, bbox_inches="tight")
print("Chart saved to data/github_chart.png")