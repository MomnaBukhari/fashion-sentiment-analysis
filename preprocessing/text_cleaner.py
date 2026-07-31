# .............................................
# This file is used to clean and preprocess text data in the dataset.
# It includes a TextCleaner class that takes a Pandas DataFrame as input and provides methods to
# combine and clean text columns.
# ..............................................


import re
import html
import unicodedata


class TextCleaner:

    def __init__(self, dataframe):
        self.df = dataframe

    def combine_text(self):

        self.df["combined_text"] = (
            self.df["caption"].astype(str)
            + " "
            + self.df["hashtag_text"].astype(str)
            + " "
            + self.df["mentions"]
            .apply(
                lambda x:
                " ".join(x)
                if isinstance(x, list)
                else str(x)
            )
        )

        # Remove duplicate words caused by hashtags
        self.df["combined_text"] = (
            self.df["combined_text"]
            .apply(
                lambda x:
                " ".join(
                    dict.fromkeys(
                        x.split()
                    )
                )
            )
        )

        return self.df

    def clean_text(self):

        def clean(sentence):

            sentence = str(sentence)

            # Lowercase
            sentence = sentence.lower()

            # Decode HTML characters
            sentence = html.unescape(sentence)

            # Unicode normalization
            sentence = unicodedata.normalize(
                "NFKD",
                sentence
            )

            # Remove URLs
            sentence = re.sub(
                r"http\S+|www\S+",
                "",
                sentence
            )

            # Remove mentions
            sentence = re.sub(
                r"@\w+",
                "",
                sentence
            )

            # Keep multilingual characters
            sentence = re.sub(
                r"[^\w\s]",
                " ",
                sentence,
                flags=re.UNICODE
            )

            # Remove extra spaces
            sentence = re.sub(
                r"\s+",
                " ",
                sentence
            )

            return sentence.strip()

        self.df["clean_text"] = (
            self.df["emoji_text"]
            .apply(clean)
        )

        # Additional simple features

        self.df["text_length"] = (
            self.df["clean_text"]
            .str.len()
        )

        self.df["mention_count"] = (
            self.df["mentions"]
            .apply(
                lambda x:
                len(x)
                if isinstance(x, list)
                else 0
            )
        )

        return self.df
