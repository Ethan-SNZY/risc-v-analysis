# RISC-V-Analysis - Semiconductor Trend Tracker

# What this is
A data piepline that tracks trend momentum in open sourced RISC-V hardware
against ARM and x86. This tracking cross references two sources, those being Google Trends Search interest (Public interest)
vs GitHub stars and commit frequency (Developer activity). These two sources are used to distiguish between actual growth of the hardware against hype.

Using this raw trend and API data, 
corresponding visualizations are produced, which allow us to identify when interest spikes, and therefore uncover a story.

## Why I built it
 While diving into the Semiconductor IP industry, I was fascinated by RISC-V's open source ISA, and it's potential to innovate the AI stack. To get a better picture of that possible future, I created this project to compare RISC-V traction against established architectures: ARM & x86, while also building upon my data extraction and analysis skills.

## Early Findings --> Only Google Trends Data @ the moment

[Search Interest Chart](data/trends_chart.png)

###RISC-V showing slow but upwards momentum
Search interest for RISC-V grew from ~7 (Jun 2025) to a peak of ~40 (Jun 2026). This is roughly a 471.43% increase in over 1 year. While causation and correlation are entirely different, this aligns with a growing adoption and preference towards customizability.

###ARM search interest satying relatively flat
Relative interest in ARM architecture as a search term stayed in the ~4–22 range throughout the period. This suggests that while ARM remains dominant in deployment, it is not generating new search-driven curiosity at the rate RISC-V is.

###x86 Spiked sharply in May-June 2026, as result of ACE
Search interest for x86 surged from ~55 to a peak of 100 (the maximum relative score) in late May 2026, before dropping sharply. This spike correlates directly with Intel and AMD's joint announcement of ACE (AI Compute Extensions). ACE is an initiative to unify AI workloads on x86 CPUs. This kind of event-driven spike is distinct from an organic, sustained growth, but also represents opportunity and probable innovation in the x86 ecosystem.

## Notes
Google Trends uses a relative index from 0–100.100 represents the peak search interest, while all other values are proportionately assigned values relative to that within the tracked period.


## Tools & skills used
- Python (requests, pytrends, pandas, csv, datetime)
- GitHub REST API (repo stats and commit activity)
- Google Trends API (via pytrends) — weekly search interest
- SQLite (in progress)


## Status

- [x] Phase 1-2: Data ingestion pipeline (GitHub + Trends)
- [ ] Phase 3: SQLite storage and transformation
- [ ] Phase 4: Trend analysis and normalization
- [ ] Phase 5: Dashboard / visualization