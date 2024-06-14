from sentence_transformers import SentenceTransformer, util

class ModelEmbedding:
    def __init__(self):
        self.bi_encoder = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1")
        #self.bi_encoder = SentenceTransformer("nq-distilbert-base-v1")

    def encode(self, text_arr):
        return self.bi_encoder.encode(text_arr, convert_to_tensor = True, show_progress_bar=False)

    def semantic_search(self, query_embedding, corpus_embedding, top_k):
        result = util.semantic_search(
                query_embeddings = query_embedding,
                corpus_embeddings = corpus_embedding,
                top_k = top_k
        )
        return result
