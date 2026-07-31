# .............................................
# This file is used to handle duplicate rows in the dataset.
# It includes a DuplicateHandler class that takes a Pandas DataFrame as input and provides a method to
# remove duplicate rows based on a specified column.
# .............................................


class DuplicateHandler:

    def __init__(self, dataframe):
        self.df = dataframe

    def remove_duplicates(self):

        self.df = (
            self.df
            .drop_duplicates(
                subset=["post_id"]
            )
            .reset_index(drop=True)
        )

        return self.df
