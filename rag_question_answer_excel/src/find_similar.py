from ModelEmbedding import ModelEmbedding
from SimilarityFinder import *

similarity_finder = SimilarityFinder(
        db_name = "data_embedding.json",
        model_embedding = ModelEmbedding()
)

accuracy = 0.3
user_query = "What is REPLACE_ME ?"
top_k = 20
similarity_finder.print_results(user_query, top_k, accuracy)
