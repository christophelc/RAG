import numpy as np
from tinydb import TinyDB, Query
from sklearn.metrics.pairwise import cosine_similarity
import torch
import chromadb
from chromadb.utils import embedding_functions

class SimilarityFinder:
    def __init__(self, db_name, model_embedding):
        self.client = chromadb.PersistentClient(db_name)
        sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name = "multi-qa-MiniLM-L6-cos-v1")
        self.collection = self.client.get_or_create_collection(name="pdf", embedding_function= sentence_transformer_ef)

        self.model = model_embedding
        self.query = Query()

    def semantic_search(self, query, top_k, accuracy):
        results = self.collection.query(
            query_texts = [query],
            n_results = top_k
        )
        documents = results["documents"][0]
        print(documents)
        return documents

    def print_results(self, user_query, top_k, accuracy):
        results = self.semantic_search(user_query, top_k, accuracy)
        print(results)
