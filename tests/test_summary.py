import pandas as pd
from missingdata.summary import summarize_missingness

def test_summary():
    df = pd.DataFrame({
        "A": [1, None, 3],
        "B": [None, None, 3],
    })
    summary = summarize_missingness(df)
    assert summary.loc["A", "missing_count"] == 1
    assert summary.loc["B", "missing_count"] == 2
    