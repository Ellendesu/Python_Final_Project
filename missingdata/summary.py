import pandas as pd


def summarize_missingness(df):
    missing = df.isnull().sum()
    percent = (missing / len(df)) * 100
    return (
        pd.DataFrame({"missing_count": missing, "missing_percent": percent.round(2)})
        .sort_values("missing_percent", ascending=False)
    )
