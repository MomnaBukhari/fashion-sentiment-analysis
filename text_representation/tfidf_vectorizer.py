# .............................................
# This file contains the TF-IDF vectorizer implementation for generating text features.
# It includes a TFIDFVectorizer class that takes a list of texts as input and provides a method to
# transform the texts into a TF-IDF feature matrix.
# .............................................


from sklearn.feature_extraction.text import TfidfVectorizer


class TFIDFVectorizer:

    def __init__(self):
        
        self.vectorizer = TfidfVectorizer(
            max_features=5000,
            ngram_range=(1,2),
            min_df=2,
            max_df=0.95
        )


    def transform(self, texts):

        tfidf_matrix = (
            self.vectorizer
            .fit_transform(texts)
        )

        return tfidf_matrix