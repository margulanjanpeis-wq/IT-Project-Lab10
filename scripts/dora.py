import pandas as pd
import requests

REPO = "margulanjanpeis-wq/IT-Project-Lab10"

url = (
    f"https://api.github.com/repos/{REPO}"
    "/actions/workflows/ci.yml/runs"
)

response = requests.get(
    url,
    params={"per_page": 100},
    timeout=30,
)
response.raise_for_status()

runs = response.json()["workflow_runs"]
df = pd.DataFrame(runs)

if df.empty:
    print("Әзірше пайплайн деректері жоқ.")
else:
    successful = df[
        (df["conclusion"] == "success")
        & (df["head_branch"] == "main")
    ].copy()

    print("Барлық іске қосылу саны:", len(df))
    print("Сәтті іске қосылу саны:", len(successful))

    if not successful.empty:
        successful["created_at"] = pd.to_datetime(
            successful["created_at"], utc=True
        )

        weekly = (
            successful.set_index("created_at")
            .resample("W")
            .size()
        )

        print("Апталық сәтті CI іске қосылулары:")
        print(weekly)
