# .............................................
# This file is used to preprocess the raw dataset.
# It includes a main function that loads the raw JSON dataset, handles missing values, removes duplicates,
# processes hashtags, combines text columns, cleans the text, detects languages, and saves the cleaned
# dataset to a CSV file. The preprocessing steps are performed using various classes defined in separate modules.
# ..............................................


from preprocessing.language_detector import LanguageDetector
from preprocessing.emoji_processor import EmojiProcessor
from preprocessing.text_cleaner import TextCleaner
from preprocessing.hashtag_processor import HashtagProcessor
from preprocessing.duplicate_handler import DuplicateHandler
from preprocessing.missing_handler import MissingValueHandler
from config.paths import (
    RAW_DATA,
    CLEANED_DATA
)
from load_data import DataLoader
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(
    str(PROJECT_ROOT)
)


def main():
    print("\nLoading raw dataset...")
    loader = DataLoader(RAW_DATA)
    df = loader.load_json()
    print(
        f"Initial rows: {len(df)}"
    )

    # Missing values
    missing = MissingValueHandler(df)
    df = missing.handle_missing_values()

    # Remove duplicates
    duplicate = DuplicateHandler(df)
    df = duplicate.remove_duplicates()
    print(
        f"Rows after duplicate removal: {len(df)}"
    )

    # Hashtags
    hashtag = HashtagProcessor(df)
    df = hashtag.process_hashtags()

    # Combine text
    cleaner = TextCleaner(df)
    df = cleaner.combine_text()

    # Emoji processing
    emoji_processor = EmojiProcessor(df)
    df = emoji_processor.process_emojis()

    # Cleaning
    df = cleaner.clean_text()

    # Language detection
    language = LanguageDetector(df)
    df = language.detect_languages()

    # Additional features
    df["word_count"] = (
        df["clean_text"]
        .apply(
            lambda x:
            len(x.split())
        )
    )
    print(
        f"Final rows: {len(df)}"
    )

    print(
        f"Total features: {len(df.columns)}"
    )

    # Save output
    CLEANED_DATA.parent.mkdir(
        exist_ok=True
    )
    df.to_csv(
        CLEANED_DATA,
        index=False,
        encoding="utf-8"
    )

    print(
        "\nPreprocessing completed successfully."
    )
    print(
        f"Saved file: {CLEANED_DATA}"
    )


if __name__ == "__main__":
    main()
