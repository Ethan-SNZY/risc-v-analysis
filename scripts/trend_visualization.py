import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#Keep improving

# Load data
df = pd.read_csv("data/trends.csv")
df["date"] = pd.to_datetime(df["date"])


plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(14, 7))

# Trend lines
ax.plot(df["date"], df["RISC-V"],
        label="RISC-V", color="#2563EB", linewidth=2)
#Shade testing
ax.fill_between(df["date"], df["RISC-V"], color="#2563EB", alpha=0.07)
ax.plot(df["date"], df["ARM architecture"],
        label="ARM Architecture", color="#DC2626", linewidth=2)
ax.plot(df["date"], df["x86"],
        label="x86", color="#16A34A", linewidth=2, linestyle="--")

#12 month average lines
riscv_avg = df["RISC-V"].mean()
x86_avg = df["x86"].mean()

ax.axhline(riscv_avg, color="#2563EB", linestyle="--", linewidth=0.8)
ax.axhline(x86_avg, color="#16A34A", linestyle="--", linewidth=0.8)

#Labelling average lines
ax.text(df["date"].iloc[1], riscv_avg + 1.5, f"RISC-V Avg: {riscv_avg:.2f}", color="#2563EB", fontsize=8)
ax.text(df["date"].iloc[1], x86_avg + 1.5, f"x86 Avg: {x86_avg:.2f}", color="#16A34A", fontsize=8)

# x86 Spike
ace_date = pd.Timestamp("2026-06")
ax.axvline(ace_date, color="gray", linestyle="--", linewidth=1)

#Newlabel
ax.text(ace_date + pd.Timedelta(days=5), 100, "Intel/AMD ACE\nAnnouncement", color="gray", 
        fontsize=8.5, rotation=0, va="bottom", ha="right",
        bbox = dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="lightgray", alpha=0.5))


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