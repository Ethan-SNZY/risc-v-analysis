import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
df = pd.read_csv("data/trends.csv")
df["date"] = pd.to_datetime(df["date"])


plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(13, 6))

# Trend lines
ax.plot(df["date"], df["RISC-V"],
        label="RISC-V", color="#2563EB", linewidth=2)
ax.plot(df["date"], df["ARM architecture"],
        label="ARM Architecture", color="#DC2626", linewidth=2)
ax.plot(df["date"], df["x86"],
        label="x86", color="#16A34A", linewidth=2, linestyle="--")

# x86 Spike
ax.annotate("x86 spike\n(May–Jun 2026)",
            xy=(pd.Timestamp("2026-05-31"), 99),
            xytext=(pd.Timestamp("2026-02-01"), 90),
            arrowprops=dict(arrowstyle="->", color="gray"),
            fontsize=9, color="gray")

# Axis Formatting
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.xticks(rotation=45)
ax.set_ylim(0, 110)
ax.set_xlabel("Date", fontsize=11)
ax.set_ylabel("Relative Search Interest (0–100)", fontsize=11)

# Labels
ax.set_title("Semiconductor Architecture Search Interest: RISC-V vs ARM vs x86\n"
             "Google Trends · June 2025 – June 2026",
             fontsize=13, fontweight="bold", pad=15)

ax.legend(loc="upper left", fontsize=10)


fig.text(0.99, 0.01,
         "Source: Google Trends · Values are relative (100 = peak interest in period)",
         ha="right", fontsize=8, color="gray")

plt.tight_layout()
plt.savefig("data/trends_chart.png", dpi=150, bbox_inches="tight")
print("Chart saved to data/trends_chart.png")