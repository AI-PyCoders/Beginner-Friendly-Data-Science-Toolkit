import pandas as pd


def handle_missing_values(df, strategy="mean"):
    numeric_cols = df.select_dtypes(
        include=['float64', 'int64']).columns.tolist()
    for col in numeric_cols:
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == "mode":
            df[col].fillna(df[col].mode()[0], inplace=True)
    return df


def remove_duplicates(df, subset=None):
    return df.drop_duplicates(subset=subset)
