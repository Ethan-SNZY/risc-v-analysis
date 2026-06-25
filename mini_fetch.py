import requests

response = requests.get("https://api.github.com/repos/lowRISC/ibex")
data = response.json()
print(data["stargazers_count"])

