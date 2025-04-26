# Final Project: Missing Data Analyzer 
**Missing Data Analyzer** is a Python library and CLI tool for detecting, summarizing, and visualizing missing data in tabular datasets (CSV format). It helps users understand the extent of missingness in their data and offers clean, interpretable summaries and visual diagnostics. 

# Group Members & Responsibilities 
- Ellen Wu: Visualizer, visualizer test file, interface for program (run_analysis.py)
- Isabella Xu: Analyzer test file, README.md, simulated data generator
- Achint Kaur: Analyzer file, overall structure 

# Features 
- Load tabular data (CSV) and detect missing values
- Compute summary statistics for missingness (per column and per row)
- Generate visualizations:
  - Bar plot of missing percentages per column
  - Heatmap of missing values across rows and columns
  - Box plot
- CLI interface for fast analysis from the terminal
- Modular Python package with reusable components
- Test suite with high coverage
- Clean codebase using `ruff` and continuous integration via GitHub Actions 

# Repository Structure
```text Python_Final_Project/
├── missingdata/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── loader.py
│   ├── summary.py
│   ├── visualizer.py
├── tests/
│   ├── test_summary.py 
│   ├── test_analyzer.py 
│   ├── test_visualizer.py 
├── cli.py
├── run_analysis.py
├── generate_simulated_data.py
├── requirements.txt
├── pyproject.toml
├── README.md
├── .github/
│   └── workflows/
│       └── ci.yml
```

# Sample simulations
## From dataset in BIOSTAT 706 (frmgham2.csv)
![image](https://github.com/user-attachments/assets/fa86724c-2b27-47d7-b4d5-addbcfd3b773)


## From ```generate_simulated_data.py
