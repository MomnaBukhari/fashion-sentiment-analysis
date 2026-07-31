# .............................................
# This file is used to create engagement features in the dataset.
# It includes an EngagementFeatures class that takes a Pandas DataFrame as input and provides a method to
# create new features related to engagement, such as engagement score, likes per follower, comments per follower,
# comment-to-like ratio, like-to-comment ratio, and engagement level.
# .............................................


import pandas as pd
import numpy as np


class EngagementFeatures:

    def __init__(self, dataframe):
        self.df = dataframe

    def create_features(self):

        # Total engagement
        self.df["engagement_score"] = (
            self.df["likes"] +
            self.df["comments"]
        )

        # Likes per follower
        self.df["likes_per_follower"] = (
            self.df["likes"] /
            (self.df["profile_followers"] + 1)
        )

        # Comments per follower
        self.df["engagement_rate"] = (
            self.df["engagement_score"] /
            (self.df["profile_followers"] + 1)
        )

        # Comment-to-like ratio
        self.df["comment_like_ratio"] = (
            self.df["comments"] /
            (self.df["likes"] + 1)
        )

        # Like-to-comment ratio
        self.df["like_comment_ratio"] = (
            self.df["likes"] /
            (self.df["comments"] + 1)
        )

        # Engagement category
        self.df["engagement_level"] = pd.cut(
            self.df["engagement_rate"],
            bins=[-np.inf, 0.05, 0.10, np.inf],
            labels=["Low", "Medium", "High"]
        )

        return self.df
