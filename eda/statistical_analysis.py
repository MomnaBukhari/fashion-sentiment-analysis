# .............................................
# This file performs statistical analysis on
# the feature engineered fashion dataset.
# It generates summary statistics required
# for exploratory data analysis.
# .............................................


import pandas as pd


class StatisticalAnalysis:


    def __init__(self, dataframe):

        self.df = dataframe



    def basic_statistics(self):

        statistics = self.df.describe(
            include="all"
        )

        return statistics



    def missing_value_analysis(self):

        missing = (
            self.df
            .isnull()
            .sum()
            .reset_index()
        )

        missing.columns = [
            "column",
            "missing_count"
        ]

        missing["missing_percentage"] = (
            missing["missing_count"]
            /
            len(self.df)
            *
            100
        )

        return missing



    def language_statistics(self):

        language_stats = (
            self.df["primary_language"]
            .value_counts()
            .reset_index()
        )

        language_stats.columns = [
            "language",
            "count"
        ]

        return language_stats



    def engagement_statistics(self):

        engagement_stats = (
            self.df[
                [
                    "likes",
                    "comments",
                    "engagement_score",
                    "likes_per_follower"
                ]
            ]
            .describe()
        )

        return engagement_stats



    def save_statistics(
        self,
        output_path
    ):

        output_path.mkdir(
            exist_ok=True
        )


        self.basic_statistics().to_csv(
            output_path /
            "basic_statistics.csv"
        )


        self.missing_value_analysis().to_csv(
            output_path /
            "missing_values.csv",
            index=False
        )


        self.language_statistics().to_csv(
            output_path /
            "language_statistics.csv",
            index=False
        )


        self.engagement_statistics().to_csv(
            output_path /
            "engagement_statistics.csv"
        )


        print(
            "Statistical analysis saved successfully."
        )