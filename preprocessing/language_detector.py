# .............................................
# This file is used to detect the language of the text in the dataset.
# It includes a LanguageDetector class that takes a Pandas DataFrame as input and provides a
# method to detect the language of the text using the Lingua library.
# The detected language is added as a new column in the DataFrame.
# ..............................................


from lingua import Language, LanguageDetectorBuilder


class LanguageDetector:

    def __init__(self, dataframe):

        self.df = dataframe

        languages = [
            Language.ENGLISH,
            Language.ARABIC,
            Language.URDU,
            Language.FRENCH,
            Language.SPANISH,
            Language.GERMAN,
            Language.ITALIAN,
        ]

        self.detector = (
            LanguageDetectorBuilder
            .from_languages(*languages)
            .build()
        )

    def detect_languages(self):

        detected = []
        primary = []
        multilingual = []

        language_map = {

            "en": "english",
            "ur": "urdu",
            "ar": "arabic",
            "es": "spanish",
            "fr": "french",
            "de": "german",
            "it": "italian"

        }

        for _, row in self.df.iterrows():

            text = row.get("clean_text", "")

            hint = str(
                row.get(
                    "language_hint",
                    ""
                )
            ).lower()

            # -------------------------
            # Language detection
            # -------------------------

            if (
                not isinstance(text, str)
                or len(text.strip()) < 3
            ):

                detected_language = "unknown"

            else:

                result = (
                    self.detector
                    .detect_language_of(text)
                )

                if result:

                    detected_language = (
                        result.name.lower()
                    )

                else:

                    detected_language = "unknown"

            detected.append(
                detected_language
            )

            # -------------------------
            # Research multilingual label
            # -------------------------

            if hint.startswith("mixed"):

                primary.append(
                    "mixed"
                )

                multilingual.append(
                    True
                )

            elif hint in language_map:

                primary.append(
                    language_map[hint]
                )

                multilingual.append(
                    False
                )

            else:

                primary.append(
                    detected_language
                )

                multilingual.append(
                    False
                )

        self.df["detected_language"] = detected

        self.df["primary_language"] = primary

        self.df["is_multilingual"] = multilingual

        return self.df
