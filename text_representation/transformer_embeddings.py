# .............................................
# This file contains the Transformer embeddings implementation for generating text features.
# It includes a TransformerEmbedding class that takes a list of texts as input and provides a method
# to transform the texts into embeddings using a pre-trained transformer model.
# ..............................................



from sentence_transformers import SentenceTransformer


class TransformerEmbedding:

    def __init__(self):

        self.model = SentenceTransformer(
            "paraphrase-multilingual-mpnet-base-v2"
        )


    def transform(self, texts):

        embeddings = (
            self.model
            .encode(
                texts,
                show_progress_bar=True
            )
        )

        return embeddings