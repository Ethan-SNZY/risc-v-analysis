import requests
import csv

repos = ["lowRISC/ibex", "riscv/riscv-isa-manual"]

results = []

for repo in repos:
	url = "https://api.github.com/repos/" + repo
	response = requests.get(url)
	data = response.json()
	stars = data["stargazers_count"]
	results.append([repo, stars])
	print(repo, "->", stars)

with open("stars.csv", "w", newline="") as f:
	writer = csv.writer(f)
	writer.writerow(["repo", "stars"])
	writer.writerows(results)

print("Saved to stars.csv")

