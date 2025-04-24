import argparse
from missingdata.analyzer import MissingDataAnalyzer


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze missing data in a CSV file."
    )
    parser.add_argument("file", help="Path to the input CSV file")
    parser.add_argument(
        "--report",
        action="store_true",
        help="Print a text summary report of missing data",
    )
    parser.add_argument(
        "--save-report",
        type=str,
        help="Optional: path to save the summary report (e.g., report.txt)",
    )
    parser.add_argument(
        "--visualize",
        action="store_true",
        help="Show a bar chart of missing values per column",
    )
    parser.add_argument(
        "--save-plot",
        type=str,
        help="Optional: path to save the plot as an image (e.g., plot.png)",
    )
    args = parser.parse_args()

    analyzer = MissingDataAnalyzer(args.file)
    analyzer.load_data()
    analyzer.compute_missing_stats()

    if args.report or args.save_report:
        report = analyzer.get_summary_report(to_file=args.save_report)
        if args.report:
            print(report)

    if args.visualize or args.save_plot:
        analyzer.plot_missing_bar(save_path=args.save_plot)


if __name__ == "__main__":
    main()

