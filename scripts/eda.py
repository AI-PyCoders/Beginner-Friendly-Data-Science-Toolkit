import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def summary_statistics(df):
    return df.describe()


def plot_correlation_matrix(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()
