import matplotlib.pyplot as plt


def plot_histogram(df, column):
    plt.figure(figsize=(8, 6))
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.show()


def plot_scatter(df, x, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(df[x], df[y], alpha=0.7)
    plt.title(f'Scatter Plot of {y} vs {x}')
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid()
    plt.show()
