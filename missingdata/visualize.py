import matplotlib.pyplot as plt
import seaborn as sns

def plot_missing_bar(df, save_path=None):
    summary = df.isnull().mean().sort_values(ascending=False)
    summary.plot(kind='bar', figsize=(10, 5), title="Missing % per Column")
    plt.ylabel("Fraction Missing")
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

