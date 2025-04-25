import matplotlib.pyplot as plt
import seaborn as sns

def plot_missing_bar(df, save_path=None):
    """
    Generate a bar plot showing missing value percentages per column.
    
    Args:
        df: pandas DataFrame to analyze
        save_path: Optional path to save the plot
    """
    summary = df.isnull().mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    summary.plot(kind='bar', color='salmon')
    plt.title("Missing % per Column")
    plt.ylabel("Fraction Missing")
    plt.xlabel("Columns")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

def plot_missing_heatmap(df, save_path=None):
    """
    Generate a heatmap showing missing values across rows and columns.
    
    Args:
        df: pandas DataFrame to analyze
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
    plt.title("Missing Values Heatmap")
    plt.xlabel("Columns")
    plt.ylabel("Rows")
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

def plot_missing_box(df, save_path=None):
    """
    Generate a box plot showing distribution of missing values per column.
    
    Args:
        df: pandas DataFrame to analyze
        save_path: Optional path to save the plot
    """
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df.isnull().melt(var_name='columns', value_name='missing'), 
                x='columns', y='missing', color='salmon',
                orient='v')  # Explicitly set orientation
    plt.title("Missing Values Distribution per Column")
    plt.xlabel("Columns")
    plt.ylabel("Fraction Missing")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()