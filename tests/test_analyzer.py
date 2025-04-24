from pathlib import Path

import pandas as pd
import pytest

from missingdata.analyzer import MissingDataAnalyzer


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """
    Create a temporary CSV file with some missing values for testing.
    """
    df = pd.DataFrame({
        "A": [1, None, 3],
        "B": [None, 2, 3],
        "C": ["x", "y", None]
    })
    file_path = tmp_path / "test_data.csv"
    df.to_csv(file_path, index=False)
    return file_path


def test_load_data(sample_csv: Path) -> None:
    analyzer = MissingDataAnalyzer(sample_csv)
    analyzer.load_data()
    assert analyzer.df is not None
    assert analyzer.df.shape == (3, 3)


def test_compute_missing_stats(sample_csv: Path) -> None:
    analyzer = MissingDataAnalyzer(sample_csv)
    analyzer.load_data()
    stats = analyzer.compute_missing_stats()

    assert isinstance(stats, dict)
    assert "columns" in stats
    assert "rows" in stats
    assert "overall" in stats
    assert stats["overall"]["total_missing"] == 3


def test_summary_report_returns_string(sample_csv: Path) -> None:
    analyzer = MissingDataAnalyzer(sample_csv)
    analyzer.load_data()
    analyzer.compute_missing_stats()
    report = analyzer.get_summary_report()
    assert isinstance(report, str)
    assert "MISSING DATA ANALYSIS REPORT" in report
    assert "Missing Count" in report


def test_summary_report_saves_file(tmp_path: Path, sample_csv: Path) -> None:
    analyzer = MissingDataAnalyzer(sample_csv)
    analyzer.load_data()
    analyzer.compute_missing_stats()
    report_file = tmp_path / "report.txt"
    analyzer.get_summary_report(to_file=report_file)

    assert report_file.exists()
    with open(report_file) as f:
        contents = f.read()
        assert "MISSING DATA ANALYSIS REPORT" in contents


def test_plot_missing_bar_runs(tmp_path: Path, sample_csv: Path) -> None:
    analyzer = MissingDataAnalyzer(sample_csv)
    analyzer.load_data()
    analyzer.compute_missing_stats()
    plot_path = tmp_path / "missing_plot.png"

    analyzer.plot_missing_bar(save_path=plot_path)
    assert plot_path.exists()
