# .............................................
# This file runs the feature engineering pipeline.
# It loads the cleaned dataset, generates engagement
# and temporal features, selects required features,
# and saves the final model-ready dataset.
# ..............................................

import sys
from pathlib import Path


# Add project root before importing project modules
PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)


from feature_engineering.dataset_selector import DatasetSelector
from feature_engineering.temporal_features import TemporalFeatures
from feature_engineering.engagement_features import EngagementFeatures

from config.paths import (
    CLEANED_DATA,
    FEATURE_DATA
)

from preprocessing.load_data import DataLoader



def main():

    print("\nLoading cleaned dataset...")

    print(
        f"Looking for file:\n{CLEANED_DATA}"
    )


    loader = DataLoader(
        CLEANED_DATA
    )

    df = loader.load_csv()


    print(
        f"Rows: {len(df)}"
    )


    # -----------------------------
    # Engagement features
    # -----------------------------

    engagement = EngagementFeatures(df)

    df = engagement.create_features()


    # -----------------------------
    # Temporal features
    # -----------------------------

    temporal = TemporalFeatures(df)

    df = temporal.create_features()


    # -----------------------------
    # Select model features
    # -----------------------------

    selector = DatasetSelector(df)

    df = selector.select_features()



    # -----------------------------
    # Save feature dataset
    # -----------------------------

    FEATURE_DATA.parent.mkdir(
        exist_ok=True
    )


    df.to_csv(
        FEATURE_DATA,
        index=False,
        encoding="utf-8"
    )


    print(
        "\nFeature engineering completed."
    )

    print(
        f"Rows: {len(df)}"
    )

    print(
        f"Columns: {len(df.columns)}"
    )

    print(
        f"Saved: {FEATURE_DATA}"
    )



if __name__ == "__main__":
    main()