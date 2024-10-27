import pandas as pd

def handle_missing_values(df, strategy="mean", columns=None):
    if columns is None:
        columns = df.columns
    for col in columns:
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == "mode":
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif strategy == "drop":
            df.dropna(subset=[col], inplace=True)
        else:
            raise ValueError("Invalid strategy. Choose 'mean', 'median', 'mode', or 'drop'.")
    return df

def remove_duplicates(df, subset=None):
    return df.drop_duplicates(subset=subset)
