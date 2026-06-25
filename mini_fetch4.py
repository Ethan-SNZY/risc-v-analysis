
import requests
import csv
from datetime import datetime, timedelta, timezone

repos = ["lowRISC/ibex", "riscv/riscv-isa-manual"]

results = []
thirty_days_ago = datetime.now(timezone.utc) - timedelta(days=30)

for repo in repos:
    # Star count
    url = "https://api.github.com/repos/" + repo
    response = requests.get(url)
    data = response.json()
    stars = data["stargazers_count"]

    # Fetch commits within 30 days
    commits_url = "https://api.github.com/repos/" + repo + "/commits"
    commits_response = requests.get(commits_url)
    commits_data = commits_response.json()

    recent_commit_count = 0
    for commit in commits_data:
        date_str = commit["commit"]["author"]["date"]
        commit_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        if commit_date > thirty_days_ago:
            recent_commit_count = recent_commit_count + 1

    results.append([repo, stars, recent_commit_count])
    print(repo, "-> stars:", stars, "| recent commits:", recent_commit_count)

with open("stars_and_commits.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["repo", "stars", "recent_commits"])
    writer.writerows(results)

print("Saved to stars_and_commits.csv")


