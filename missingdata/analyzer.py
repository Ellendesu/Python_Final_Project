"""Basic Layout of Analyzer."""
from typing import Dict, List, Optional, Tuple, Union
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
from pathlib import Path
class MissingDataAnalyzer:
    """Main class for missing data analysis operations."""
    
    def __init__(self, file_path: Union[str, Path]) -> None:
        """
        Initialize the analyzer with a data file.
        
        Args:
            file_path: Path to the CSV file to analyze
        """
        self.file_path = Path(file_path)
        self.df: Optional[pd.DataFrame] = None
        self.missing_stats: Optional[Dict[str, Dict[str, float]]] = None
        
    def load_data(self) -> None:
        """Load data from CSV file into a pandas DataFrame."""
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"Successfully loaded data with {self.df.shape[0]} rows and {self.df.shape[1]} columns.")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def compute_missing_stats(self) -> Dict[str, Dict[str, float]]:
        """
        Compute comprehensive missing data statistics.
        
        Returns:
            Dictionary containing missing data statistics at both column and row levels
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # Column-wise statistics
        col_missing = self.df.isna().mean() * 100
        col_missing_counts = self.df.isna().sum()
        
        # Row-wise statistics
        row_missing = self.df.isna().mean(axis=1) * 100
        row_missing_counts = self.df.isna().sum(axis=1)
        
        self.missing_stats = {
            'columns': {
                'percent_missing': col_missing.to_dict(),
                'missing_counts': col_missing_counts.to_dict()
            },
            'rows': {
                'percent_missing': row_missing.to_dict(),
                'missing_counts': row_missing_counts.to_dict()
            },
            'overall': {
                'total_missing': self.df.isna().sum().sum(),
                'total_cells': self.df.size,
                'pct_missing': (self.df.isna().sum().sum() / self.df.size) * 100
            }
        }
        
        return self.missing_stats
    
    def get_summary_report(self) -> str:
        """
        Generate a human-readable summary report of missing data.
        
        Returns:
            Formatted string with missing data summary
        """
        if self.missing_stats is None:
            self.compute_missing_stats()
            
        report = []
        report.append("=" * 50)
        report.append("MISSING DATA ANALYSIS REPORT")
        report.append("=" * 50)
        report.append(f"\nDataset: {self.file_path.name}")
        report.append(f"Total rows: {self.df.shape[0]}")
        report.append(f"Total columns: {self.df.shape[1]}")
        report.append(f"Total missing values: {self.missing_stats['overall']['total_missing']}")
        report.append(f"Percentage missing: {self.missing_stats['overall']['pct_missing']:.2f}%")
        
        report.append("\nCOLUMN-WISE ANALYSIS:")
        col_stats = pd.DataFrame({
            'Missing Count': self.missing_stats['columns']['missing_counts'],
            'Missing %': self.missing_stats['columns']['percent_missing']
        })
        report.append(col_stats.sort_values('Missing %', ascending=False).to_string())
        
        return "\n".join(report)
    



#if __name__ == "__main__":
    #import sys
    #sys.exit(main())