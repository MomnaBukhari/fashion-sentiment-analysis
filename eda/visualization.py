# .............................................
# This file contains visualization functions for
# exploratory data analysis of fashion trend data.
# It generates plots for distributions and patterns.
# .............................................


import matplotlib.pyplot as plt
import seaborn as sns


class Visualizer:

    def __init__(self, dataframe, output_path):
        self.df = dataframe
        self.output_path = output_path


    def plot_language_distribution(self):

        plt.figure(figsize=(8,5))

        sns.countplot(
            data=self.df,
            x="primary_language",
            order=self.df["primary_language"].value_counts().index
        )

        plt.xticks(
            rotation=45
        )

        plt.title(
            "Language Distribution"
        )

        plt.tight_layout()

        plt.savefig(
            self.output_path / "language_distribution.png"
        )

        plt.close()



    def plot_multilingual_distribution(self):

        plt.figure(figsize=(6,4))

        sns.countplot(
            data=self.df,
            x="is_multilingual"
        )

        plt.title(
            "Multilingual vs Monolingual Posts"
        )

        plt.tight_layout()

        plt.savefig(
            self.output_path / "multilingual_distribution.png"
        )

        plt.close()



    def plot_engagement_distribution(self):

        plt.figure(figsize=(8,5))

        sns.histplot(
            data=self.df,
            x="engagement_score",
            bins=30
        )

        plt.title(
            "Engagement Score Distribution"
        )

        plt.tight_layout()

        plt.savefig(
            self.output_path / "engagement_distribution.png"
        )

        plt.close()