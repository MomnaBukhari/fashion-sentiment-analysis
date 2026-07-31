# .............................................
# This file is used to process emojis in the dataset.
# It includes an EmojiProcessor class that takes a Pandas DataFrame as input and provides a method to
# detect and count emojis in the text.
# ..............................................


import emoji


class EmojiProcessor:

    def __init__(self, dataframe):
        self.df = dataframe

    def process_emojis(self):
        self.df["emoji_text"] = (
            self.df["combined_text"]
            .apply(
                lambda x:
                emoji.demojize(
                    x,
                    delimiters=(" ", " ")
                )
            )
        )
        self.df["emoji_count"] = (

            self.df["combined_text"]
            .apply(
                lambda x:
                sum(
                    1
                    for char in x
                    if char in emoji.EMOJI_DATA
                )
            )

        )
        return self.df