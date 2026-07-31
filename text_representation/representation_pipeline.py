# .............................................
# This file contains the pipeline for generating text representations.
# It includes functions for TF-IDF vectorization and transformer embeddings.
# .............................................


import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(PROJECT_ROOT)
)


import pandas as pd

from config.paths import FEATURE_DATA


from text_representation.tfidf_vectorizer import TFIDFVectorizer



OUTPUT_PATH = (
    PROJECT_ROOT /
    "data" /
    "features" /
    "tfidf_features.csv"
)



def main():


    print("\nLoading feature dataset...")


    df = pd.read_csv(
        FEATURE_DATA
    )


    print(
        f"Rows: {len(df)}"
    )


    texts = (
        df["clean_text"]
        .fillna("")
    )


    vectorizer = TFIDFVectorizer()


    tfidf_matrix = (
        vectorizer
        .transform(texts)
    )


    tfidf_df = pd.DataFrame(
        tfidf_matrix.toarray()
    )


    tfidf_df.to_csv(
        OUTPUT_PATH,
        index=False
    )


    print(
        "\nTF-IDF completed"
    )


    print(
        f"Shape: {tfidf_df.shape}"
    )


    print(
        f"Saved: {OUTPUT_PATH}"
    )



if __name__ == "__main__":
    main()