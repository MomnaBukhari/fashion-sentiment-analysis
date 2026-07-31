# .............................................
# This file is used to select specific features from the dataset for further analysis.
# It includes a DatasetSelector class that takes a Pandas DataFrame as input and provides a method to
# select a predefined set of features from the DataFrame.
# .............................................


class DatasetSelector:

    def __init__(self, dataframe):
        self.df = dataframe

    def select_features(self):

        columns = [

            "post_id",

            "clean_text",

            "fashion_category",

            "primary_language",

            "is_multilingual",

            "location",

            "profile_verified",

            "profile_followers",

            "likes",

            "comments",

            "engagement_score",

            "likes_per_follower",

            "comment_like_ratio",

            "engagement_level",

            "word_count",

            "emoji_count",

            "hashtag_count",

            "mention_count",

            "text_length",

            "year",

            "month",

            "day",

            "hour",

            "weekday",

            "is_weekend"

        ]

        return self.df[columns]
