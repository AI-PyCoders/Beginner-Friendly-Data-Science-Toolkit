import matplotlib.pyplot as plt


def plot_histogram(df, column):
    plt.figure(figsize=(8, 6))
    plt.hist(df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()


def plot_scatter(df, x_column, y_column):
    plt.figure(figsize=(8, 6))
    plt.scatter(df[x_column], df[y_column],
                color='blue', edgecolor='k', alpha=0.7)
    plt.title(f'Scatter Plot of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()
