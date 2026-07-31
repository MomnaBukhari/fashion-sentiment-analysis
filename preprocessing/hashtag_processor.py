# .............................................
# This file is used to process hashtags in the dataset.
# It includes a HashtagProcessor class that takes a Pandas DataFrame as input and provides a method to
# extract and count hashtags from the text.
# ..............................................


import re


class HashtagProcessor:

    def __init__(self, dataframe):
        self.df = dataframe

    def process_hashtags(self):

        def extract_hashtags(row):

            hashtags = []

            if isinstance(row["hashtags"], list):

                hashtags.extend(row["hashtags"])

            if isinstance(row["caption"], str):

                hashtags.extend(
                    re.findall(
                        r"#(\w+)",
                        row["caption"],
                        flags=re.UNICODE
                    )
                )

            return list(set(hashtags))

        self.df["hashtags"] = (
            self.df.apply(
                extract_hashtags,
                axis=1
            )
        )

        self.df["hashtag_text"] = (
            self.df["hashtags"]
            .apply(
                lambda x: " ".join(x)
            )
        )

        self.df["hashtag_count"] = (
            self.df["hashtags"]
            .apply(len)
        )

        return self.df
