import pandas as pd

def load_csv(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath, na_values=["NA", "N/A", ".", ""])
