# .............................................
# This file is used to inspect the dataset and provide basic information about it.
# It includes functions to check for missing values, duplicates, and the distribution of languages and fashion
# categories in the dataset. It also provides a summary of numeric columns.
# .............................................


import pandas as pd

class DataInspector:

    def __init__(self, dataframe):
        self.df = dataframe

    def basic_information(self):
        print("\n========== BASIC INFORMATION ==========\n")
        print(f"Rows: {self.df.shape[0]}")
        print(f"Columns: {self.df.shape[1]}")
        print("\nColumn Names:\n")
        for column in self.df.columns:
            print(column)
        print("\nData Types:\n")
        print(self.df.dtypes)
        
    def missing_values(self):
        print("\n========== MISSING VALUES ==========\n")
        print(self.df.isnull().sum())

    def duplicate_rows(self):
        print("\n========== DUPLICATES POST IDS ==========\n")
        duplicates = self.df.duplicated(subset=["post_id"]).sum()
        print(f"Duplicate Rows: {duplicates}")

    def language_distribution(self):
        print("\n========== LANGUAGE DISTRIBUTION ==========\n")
        print(
            self.df["language_hint"].value_counts(dropna=False)
        )

    def fashion_categories(self):
        print("\n========== FASHION CATEGORIES ==========\n")
        print(
            self.df["fashion_category"].value_counts(dropna=False)
        )

    def numeric_summary(self):
        print("\n========== NUMERIC SUMMARY ==========\n")
        print(
            self.df.describe(include="number")
        )

    def run_all(self):
        self.basic_information()
        self.missing_values()
        self.duplicate_rows()
        self.language_distribution()
        self.fashion_categories()
        self.numeric_summary()