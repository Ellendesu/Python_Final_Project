import matplotlib.pyplot as plt
import seaborn as sns

def plot_missing_bar(df, save_path=None):
    """Fixed bar plot of missing percentages"""
    missing_pct = df.isnull().mean().sort_values(ascending=False) * 100
    
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x=missing_pct.index, y=missing_pct.values, color='salmon')
    
    plt.title("Missing Data Percentage by Column", fontsize=14)
    plt.ylabel("Percentage Missing")
    plt.ylim(0, 100)  # Proper percentage scale
    
    # Add value labels
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width()/2., height + 1,
                f'{height:.1f}%', ha='center')
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.close()
    else:
        plt.show()

def plot_missing_heatmap(df, save_path=None):
    """Heatmap of missing values"""
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis', 
               yticklabels=False, xticklabels=True)
    plt.title("Missing Values Heatmap", fontsize=14)
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.close()
    else:
        plt.show()

def plot_missing_box(df, save_path=None):
    """Box plot of missing value distribution"""
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df.isnull().melt(var_name='columns', value_name='missing'),
                x='columns', y='missing', color='lightblue')
    plt.title("Missing Values Distribution", fontsize=14)
    plt.xlabel("Columns")
    plt.ylabel("Missing (1 = missing)")
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
        plt.close()
    else:
        plt.show()