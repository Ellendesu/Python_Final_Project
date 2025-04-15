import argparse
from missingdata.loader import load_csv
from missingdata.summary import summarize_missingness
from missingdata.visualize import plot_missing_bar

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to CSV")
    parser.add_argument("--visualize", action="store_true")
    args = parser.parse_args()

    df = load_csv(args.file)
    print(summarize_missingness(df))

    if args.visualize:
        plot_missing_bar(df)

if __name__ == "__main__":
    main()

