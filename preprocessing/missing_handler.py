# .............................................
# This file is used to handle missing values in the dataset.
# It includes a MissingValueHandler class that takes a Pandas DataFrame as input and provides a method to
# fill missing values with appropriate defaults.
# ..............................................


class MissingValueHandler:

    def __init__(self, dataframe):
        self.df = dataframe

    def handle_missing_values(self):

        text_columns = [
            "caption",
            "hashtags",
            "mentions"
        ]
        metadata_columns = [
            "language_hint",
            "location",
            "fashion_category"
        ]

        for column in text_columns:

            if column in self.df.columns:

                self.df[column] = (
                    self.df[column]
                    .fillna("")
                )

        for column in metadata_columns:

            if column in self.df.columns:

                self.df[column] = (
                    self.df[column]
                    .fillna("unknown")
                )

        return self.df