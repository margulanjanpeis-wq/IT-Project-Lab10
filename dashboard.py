
import pandas as pd
import requests
import streamlit as st

REPO = "margulanjanpeis-wq/IT-Project-Lab10"

st.set_page_config(
    page_title="CI/CD Dashboard",
    layout="wide"
)

st.title("CI/CD және DORA дашборды")
st.write("IT жобаларды басқару — зертханалық жұмыс №10")

url = (
    f"https://api.github.com/repos/{REPO}"
    "/actions/workflows/ci.yml/runs"
)

try:
    response = requests.get(
        url,
        params={"per_page": 100},
        timeout=30
    )
    response.raise_for_status()
    runs = response.json()["workflow_runs"]

    if not runs:
        st.info("Әзірше деректер жоқ.")
    else:
        df = pd.DataFrame(runs)
        successful = df[
            (df["conclusion"] == "success")
            & (df["head_branch"] == "main")
        ].copy()

        col1, col2, col3 = st.columns(3)

        col1.metric("Барлық CI іске қосылуы", len(df))
        col2.metric("Сәтті CI", len(successful))
        col3.metric(
            "Сәттілік пайызы",
            f"{len(successful) / len(df) * 100:.1f}%"
        )

        st.subheader("Апталық CI нәтижелері")

        successful["created_at"] = pd.to_datetime(
            successful["created_at"], utc=True
        )

        if not successful.empty:
            weekly = (
                successful.set_index("created_at")
                .resample("W")
                .size()
            )
            st.bar_chart(weekly)

        st.caption(
            "CI нәтижелері deployment метрикасына "
            "тең емес. DORA көрсеткіштері кейін қосылады."
        )

except requests.RequestException as error:
    st.error(f"GitHub API қатесі: {error}")
