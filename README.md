# Final Project: Missing Data Analyzer 
**Missing Data Analyzer** is a Python library and CLI tool for detecting, summarizing, and visualizing missing data in tabular datasets (CSV format). It helps users understand the extent of missingness in their data and offers clean, interpretable summaries and visual diagnostics. 

# Group Members & Responsibilities 
Ellen Wu: Visualizer 
Isabella Xu: Analyzer 
Achint Kaur: Analyzer 

# Features 
- Load tabular data (CSV) and detect missing values
- Compute summary statistics for missingness (per column and per row)
- Generate visualizations:
  - Bar plot of missing percentages per column
  - Heatmap of missing values across rows and columns
- CLI interface for fast analysis from the terminal
- Modular Python package with reusable components
- Test suite with high coverage
- Clean codebase using `ruff` and continuous integration via GitHub Actions 

# Repository Structure
/data-analyzer
├── src/

│   ├── __init__.py

│   ├── analyzer.py        # Core analysis functions

│   ├── visualizer.py      # Visualization functions

│   └── imputer.py        # Imputation suggestions

├── tests/

│   ├── test_analyzer.py

│   ├── test_visualizer.py

│   └── test_imputer.py

├── examples/             # Sample datasets and demo notebooks

├── docs/                 # Documentation

├── pyproject.toml        # Project configuration

└── README.md
