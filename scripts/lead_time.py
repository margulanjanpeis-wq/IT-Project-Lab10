
from datetime import datetime

import requests

REPO = "margulanjanpeis-wq/IT-Project-Lab10"
BASE = f"https://api.github.com/repos/{REPO}"

response = requests.get(
    f"{BASE}/actions/workflows/ci.yml/runs",
    params={"branch": "main", "per_page": 100},
    timeout=90,
)
response.raise_for_status()

lead_times = []

for run in response.json()["workflow_runs"]:
    jobs_response = requests.get(
        run["jobs_url"],
        params={"per_page": 100},
        timeout=90,
    )
    jobs_response.raise_for_status()

    for job in jobs_response.json()["jobs"]:
        if (
            job["name"] == "Оқу стендіне орналастыру"
            and job["conclusion"] == "success"
        ):
            commit_response = requests.get(
                f"{BASE}/commits/{run['head_sha']}",
                timeout=90,
            )
            commit_response.raise_for_status()

            commit_date = commit_response.json()[
                "commit"
            ]["committer"]["date"]

            start = datetime.fromisoformat(
                commit_date.replace("Z", "+00:00")
            )
            end = datetime.fromisoformat(
                job["completed_at"].replace("Z", "+00:00")
            )

            hours = (end - start).total_seconds() / 3600
            lead_times.append(hours)

if lead_times:
    print("Lead Time нәтижелері:")
    for value in lead_times:
        print(f"{value:.2f} сағат")

    print(
        "Орташа Lead Time:",
        f"{sum(lead_times) / len(lead_times):.2f} сағат",
    )
else:
    print("Сәтті орналастыру деректері табылмады.")
