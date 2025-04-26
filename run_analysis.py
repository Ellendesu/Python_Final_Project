from missingdata.analyzer import MissingDataAnalyzer
from missingdata.visualize import plot_missing_bar, plot_missing_heatmap, plot_missing_box
from pathlib import Path

def get_user_file_path():
    """Prompt user for file path and validate it exists"""
    while True:
        file_path = input("\nEnter path to CSV file (or drag file here): ").strip()
        
        # Remove quotes if user drag-and-dropped file
        file_path = file_path.strip('"\'')
        
        path = Path(file_path)
        
        if path.exists():
            return path
        print(f"File not found: {path.absolute()}\nPlease try again.")

def analyze_simulated_data():
    try:
        print("=== Missing Data Analyzer ===")
        print("Please provide the CSV file to analyze\n")
        
        # Get file path from user
        data_path = get_user_file_path()
            
        analyzer = MissingDataAnalyzer(data_path)
        
        # Load and analyze data
        print("\nAnalyzing data...")
        analyzer.load_data()
        stats = analyzer.compute_missing_stats()
        
        # Generate and save report
        report = analyzer.get_summary_report()
        print("\nAnalysis Results:")
        print(report)
        
        # Save text report
        report_name = f"{data_path.stem}_report.txt"
        report_path = Path(report_name)
        with open(report_path, "w") as f:
            f.write(report)
        print(f"\nReport saved to: {report_path.absolute()}")
        
        # Generate all visualizations
        viz_files = {
            "Bar Plot": f"{data_path.stem}_missingness.png",
            "Heatmap": f"{data_path.stem}_heatmap.png",
            "Box Plot": f"{data_path.stem}_boxplot.png"
        }
        
        # Create visualizations
        print("\nGenerating visualizations...")
        plot_missing_bar(analyzer.df, viz_files["Bar Plot"])
        plot_missing_heatmap(analyzer.df, viz_files["Heatmap"])
        plot_missing_box(analyzer.df, viz_files["Box Plot"])
        
        print("\nVisualizations created:")
        for name, path in viz_files.items():
            print(f"- {name}: {Path(path).absolute()}")
            
        return True
    
    except Exception as e:
        print(f"\nError during analysis: {str(e)}")
        return False

if __name__ == "__main__":
    success = analyze_simulated_data()
    if not success:
        print("\nAnalysis failed. Please check the error message above.")
    else:
        print("\nAnalysis completed successfully!")
