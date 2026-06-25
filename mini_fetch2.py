import requests 

repos = ["lowRISC/ibex", "riscv/riscv-isa-manual"]

for repo in repos:
    url = "https://api.github.com/repos/" + repo
    response = requests.get(url)
    data = response.json()
    print(repo, "->", data["stargazers_count"])


