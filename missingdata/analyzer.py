"This file analyzes misisng values for the csv input."

from pathlib import Path
from typing import Any, Optional, Union

import pandas as pd
import matplotlib.pyplot as plt


class MissingDataAnalyzer:
    """
    A class for analyzing missing data in tabular (CSV) datasets.
    Provides methods for loading data, computing missing value statistics,
    generating summary reports, and creating visualizations.
    """

    def __init__(self, file_path: Union[str, Path]) -> None:
        """
        Initialize the analyzer with a path to the dataset.

        Args:
            file_path: Path to the input CSV file.
        """
        self.file_path = Path(file_path)
        self.df: Optional[pd.DataFrame] = None
        self.missing_stats: Optional[dict[str, Any]] = None

    def load_data(self) -> None:
        """
        Load the CSV dataset into a pandas DataFrame and handle standard NA representations.
        """
        try:
            self.df = pd.read_csv(self.file_path, na_values=["NA", "N/A", ".", ""])
            print(f"Loaded {self.df.shape[0]} rows and {self.df.shape[1]} columns.")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")

    def compute_missing_stats(self) -> dict[str, Any]:
        """
        Compute missing value statistics at the column, row, and overall level.

        Returns:
            Dictionary with missing data statistics.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        col_missing = self.df.isna().mean() * 100
        col_missing_counts = self.df.isna().sum()
        row_missing = self.df.isna().mean(axis=1) * 100
        row_missing_counts = self.df.isna().sum(axis=1)

        self.missing_stats = {
            'columns': {
                'percent_missing': col_missing.to_dict(),
                'missing_counts': col_missing_counts.to_dict(),
            },
            'rows': {
                'percent_missing': row_missing.to_dict(),
                'missing_counts': row_missing_counts.to_dict(),
            },
            'overall': {
                'total_missing': int(self.df.isna().sum().sum()),
                'total_cells': int(self.df.size),
                'pct_missing': float((self.df.isna().sum().sum() / self.df.size) * 100),
            },
        }

        return self.missing_stats

    def get_summary_report(self, to_file: Optional[Union[str, Path]] = None) -> str:
        """
        Generate a plain-text summary of missing values, optionally saving to file.

        Args:
            to_file: Optional path to save the report as a text file.

        Returns:
            Formatted string summary report.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        if self.missing_stats is None:
            self.compute_missing_stats()

        assert self.missing_stats is not None 

        overall = self.missing_stats["overall"]
        column_counts = self.missing_stats["columns"]["missing_counts"]
        column_percents = self.missing_stats["columns"]["percent_missing"]

        report = []
        report.append("=" * 50)
        report.append("MISSING DATA ANALYSIS REPORT")
        report.append("=" * 50)
        report.append(f"Dataset: {self.file_path.name}")
        report.append(f"Total rows: {self.df.shape[0]}")
        report.append(f"Total columns: {self.df.shape[1]}")
        report.append(f"Total missing values: {overall['total_missing']}")
        report.append(f"Percentage missing: {overall['pct_missing']:.2f}%\n")

        report.append("COLUMN-WISE ANALYSIS:")
        col_stats = pd.DataFrame({
            'Missing Count': column_counts,
            'Missing %': column_percents,
        })
        report.append(col_stats.sort_values("Missing %", ascending=False).to_string())

        final_report = "\n".join(report)

        if to_file:
            to_file = Path(to_file)
            with open(to_file, "w") as f:
                f.write(final_report)
            print(f"Report saved to {to_file}")

        return final_report

    def plot_missing_bar(self, save_path: Optional[Union[str, Path]] = None) -> None:
        """
        Generate and display (or save) a bar plot of percent missing per column.

        Args:
            save_path: Optional path to save the plot as an image.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        missing_frac = self.df.isnull().mean().sort_values(ascending=False)

        plt.figure(figsize=(10, 6))
        missing_frac.plot(kind="bar", title="Missing % per Column", color="salmon")
        plt.ylabel("Fraction Missing")
        plt.xlabel("Columns")
        plt.tight_layout()

        if save_path:
            save_path = Path(save_path)
            plt.savefig(save_path)
            print(f"Plot saved to {save_path}")
        else:
            plt.show()
