import requests

with open("source.tsv", "r") as f:
    data = requests.get(
        "https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json"
    ).json()

    found = {}

    for line in f:
        for d in data:
            if d["name"].lower() == line.strip().lower():
                with open("result.tsv", "a+") as wr:
                    name = d["name"]
                    country = d["country"]
                    wr.write(f"{name}\t{country}\n")
