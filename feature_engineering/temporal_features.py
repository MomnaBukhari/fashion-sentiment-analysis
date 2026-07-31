# .............................................
# This file is used to create temporal features from the timestamp column in the dataset.
# It includes a TemporalFeatures class that takes a Pandas DataFrame as input and provides a
# method to create new features such as year, month, day, hour, weekday, and is_weekend.
# .............................................


import pandas as pd


class TemporalFeatures:

    def __init__(self, dataframe):
        self.df = dataframe

    def create_features(self):

        self.df["timestamp"] = pd.to_datetime(
            self.df["timestamp"]
        )

        self.df["year"] = (
            self.df["timestamp"]
            .dt.year
        )

        self.df["month"] = (
            self.df["timestamp"]
            .dt.month
        )

        self.df["day"] = (
            self.df["timestamp"]
            .dt.day
        )

        self.df["hour"] = (
            self.df["timestamp"]
            .dt.hour
        )

        self.df["weekday"] = (
            self.df["timestamp"]
            .dt.day_name()
        )

        self.df["is_weekend"] = (
            self.df["weekday"]
            .isin(
                ["Saturday", "Sunday"]
            )
        )

        return self.df
