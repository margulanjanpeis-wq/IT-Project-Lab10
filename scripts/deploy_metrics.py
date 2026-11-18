
import requests

REPO = "margulanjanpeis-wq/IT-Project-Lab10"
BASE = f"https://api.github.com/repos/{REPO}"

deployments = []
page = 1

while True:
    response = requests.get(
        f"{BASE}/actions/workflows/ci.yml/runs",
        params={
            "branch": "main",
            "per_page": 100,
            "page": page,
        },
        timeout=30,
    )
    response.raise_for_status()
    runs = response.json()["workflow_runs"]

    if not runs:
        break

    for run in runs:
        jobs_url = run["jobs_url"]
        jobs_response = requests.get(
            jobs_url,
            params={"per_page": 100},
            timeout=30,
        )
        jobs_response.raise_for_status()
        jobs = jobs_response.json()["jobs"]

        for job in jobs:
            if (
                job["name"] == "Оқу стендіне орналастыру"
                and job["conclusion"] == "success"
            ):
                deployments.append(job)

    page += 1

print("Сәтті орналастыру саны:", len(deployments))

for job in deployments:
    print(job["completed_at"], "-", job["name"])
