import numpy as np
from tinydb import TinyDB, Query
from sklearn.metrics.pairwise import cosine_similarity
import torch

class SimilarityFinder:
    def __init__(self, db_name, model_embedding):
        self.db = TinyDB(db_name)
        self.model = model_embedding
        self.query = Query()

    def semantic_search(self, query, top_k, accuracy):
        query_embedding = self.model.encode(query).reshape(1, -1)
        corpus_embedding = [torch.as_tensor(item["embedding"]) for item in self.db.all()]
        hits = self.model.semantic_search(query_embedding, corpus_embedding, top_k)[0]
        iterator = filter(lambda hit: hit["score"] >= accuracy, hits)
        corpus = [data["Answers"] for data in self.db.all()] 
        results = [corpus[hit["corpus_id"]] for hit in iterator]
        return results

    def print_results(self, user_query, top_k, accuracy):
        results = self.semantic_search(user_query, top_k, accuracy)
        print(results)
