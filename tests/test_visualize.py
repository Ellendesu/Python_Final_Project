import pandas as pd
import pytest
import warnings

from missingdata.visualize import (
    plot_missing_bar,
    plot_missing_heatmap,
    plot_missing_box,
)


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "A": [1, None, 3, None, 5],
        "B": [None, 2, None, 4, 5],
        "C": ["x", "y", None, None, "z"]
    })


def test_plot_missing_bar(sample_df, tmp_path):
    plot_path = tmp_path / "missing_bar.png"
    plot_missing_bar(sample_df, save_path=plot_path)
    assert plot_path.exists()


def test_plot_missing_heatmap(sample_df, tmp_path):
    plot_path = tmp_path / "missing_heatmap.png"
    plot_missing_heatmap(sample_df, save_path=plot_path)
    assert plot_path.exists()


def test_plot_missing_box(sample_df, tmp_path):
    plot_path = tmp_path / "missing_box.png"
    # Suppress the specific warning
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=PendingDeprecationWarning)
        plot_missing_box(sample_df, save_path=plot_path)
    assert plot_path.exists()