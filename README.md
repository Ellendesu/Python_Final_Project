[simulated_missing_data_report.txt](https://github.com/user-attachments/files/19918412/simulated_missing_data_report.txt)[frmgham2 copy_report.txt](https://github.com/user-attachments/files/19918409/frmgham2.copy_report.txt)# Final Project: Missing Data Analyzer 
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
![image](https://github.com/user-attachments/assets/358ed206-8fd9-4d55-a52f-2f3ce9971cdc)
![image](https://github.com/user-attachments/assets/9af3c6bd-2ec6-450e-90a4-539419d57d63)
[Uploading ==================================================
MISSING DATA ANALYSIS REPORT
==================================================
Dataset: frmgham2 copy.csv
Total rows: 11627
Total columns: 39
Total missing values: 20075
Percentage missing: 4.43%

COLUMN-WISE ANALYSIS:
          Missing Count  Missing %
LDLC               8601  73.974370
HDLC               8600  73.965769
GLUCOSE            1440  12.384966
BPMEDS              593   5.100198
TOTCHOL             409   3.517674
educ                295   2.537198
CIGPDAY              79   0.679453
BMI                  52   0.447235
HEARTRTE              6   0.051604
TIMEAP                0   0.000000
MI_FCHD               0   0.000000
ANYCHD                0   0.000000
STROKE                0   0.000000
CVD                   0   0.000000
HYPERTEN              0   0.000000
RANDID                0   0.000000
TIMEMI                0   0.000000
ANGINA                0   0.000000
TIMEMIFC              0   0.000000
TIMECHD               0   0.000000
TIMESTRK              0   0.000000
TIMECVD               0   0.000000
TIMEDTH               0   0.000000
HOSPMI                0   0.000000
TIME                  0   0.000000
DEATH                 0   0.000000
PERIOD                0   0.000000
SEX                   0   0.000000
PREVHYP               0   0.000000
PREVSTRK              0   0.000000
PREVMI                0   0.000000
PREVAP                0   0.000000
PREVCHD               0   0.000000
DIABETES              0   0.000000
CURSMOKE              0   0.000000
DIABP                 0   0.000000
SYSBP                 0   0.000000
AGE                   0   0.000000
TIMEHYP               0   0.000000frmgham2 copy_report.txt…]()

## From generate_simulated_data.py
![image](https://github.com/user-attachments/assets/1d174460-5c9f-4b79-b2ec-3de9234d997a)
![image](https://github.com/user-attachments/assets/513b3b9a-09b4-4470-912c-21a9741f8c7e)
![image](https://github.com/user-attachments/assets/fa7e1025-24e7-49fa-878c-3b55e09d55e3)
[Uploading simulated_missin==================================================
MISSING DATA ANALYSIS REPORT
==================================================
Dataset: simulated_missing_data.csv
Total rows: 200
Total columns: 20
Total missing values: 415
Percentage missing: 10.38%

COLUMN-WISE ANALYSIS:
            Missing Count  Missing %
feature_1              29       14.5
feature_14             28       14.0
feature_16             27       13.5
feature_2              25       12.5
feature_18             24       12.0
feature_13             24       12.0
feature_3              23       11.5
feature_8              22       11.0
feature_12             21       10.5
feature_11             21       10.5
feature_20             21       10.5
feature_6              20       10.0
feature_4              20       10.0
feature_9              19        9.5
feature_7              19        9.5
feature_19             18        9.0
feature_10             15        7.5
feature_15             14        7.0
feature_5              14        7.0
feature_17             11        5.5g_data_report.txt…]()


