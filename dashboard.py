
import pandas as pd
import requests
import streamlit as st

REPO = "margulanjanpeis-wq/IT-Project-Lab10"

st.set_page_config(
    page_title="DORA Dashboard",
    layout="wide",
)

st.title("CI/CD және DORA дашборды")
st.write("IT жобаларды басқару — Зертханалық жұмыс №10")

st.subheader("DORA метрикалары")

a, b, c, d = st.columns(4)

a.metric("Deployment Frequency", "1")
b.metric("Lead Time", "0.01 сағ")
c.metric("Change Failure Rate", "0%")
d.metric("Recovery Time", "N/A")

st.caption(
    "DORA көрсеткіштері: 18.11.2026 күнгі "
    "бір сәтті оқу стенді орналастыруының нәтижелері. "
    "Lead Time — соңғы commit-тен deploy аяқталғанға дейін. "
    "Recovery Time есептелмеді, себебі инцидент жоқ."
)

st.divider()
st.subheader("GitHub Actions статистикасы")

url = (
    f"https://api.github.com/repos/{REPO}"
    "/actions/workflows/ci.yml/runs"
)

try:
    response = requests.get(
        url,
        params={"per_page": 100},
        timeout=90,
    )
    response.raise_for_status()
    runs = response.json()["workflow_runs"]

    if not runs:
        st.info("CI/CD деректері табылмады.")
    else:
        df = pd.DataFrame(runs)

        successful = df[
            (df["conclusion"] == "success")
            & (df["head_branch"] == "main")
        ].copy()

        x, y, z = st.columns(3)

        x.metric("Барлық CI", len(df))
        y.metric("Сәтті CI", len(successful))
        z.metric(
            "CI сәттілік пайызы",
            f"{len(successful) / len(df) * 100:.1f}%",
        )

        if not successful.empty:
            successful["created_at"] = pd.to_datetime(
                successful["created_at"],
                utc=True,
            )

            weekly = (
                successful.set_index("created_at")
                .resample("W")
                .size()
            )

            st.subheader("Апталық CI нәтижелері")
            st.bar_chart(weekly)

except requests.RequestException as error:
    st.error(f"GitHub API қатесі: {error}")
