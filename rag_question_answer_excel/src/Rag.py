from AnswerGenerator import *
from ModelEmbedding import ModelEmbedding
from ModelProxyAPI import *
from Reranking import *
import time

message_init = {
                "role" : "system",
                "content": """
                You are a flower assistant who answers questions in a concise style. Provide answers only according to the following sentences starting with 'kw:'.
                """
}

class Rag:
    def __init__(
            self,
            model_embedding = ModelEmbedding(),
            llm_proxy = ModelProxyAPI()        
    ):
        self.gen = AnswerGenerator(
                db_name = "data_embedding.json",
                model_embedding = model_embedding,
                cross_encoder = cross_encoder,
                accuracy = 0.3,
                rag_top_n = 20,
                rerank_accuracy = 0.1,
                max_token = 300,
                llm_proxy = llm_proxy
        )

    def query(self, user_query, history):
        start_time = time.time()
        answer = self.gen.run(user_query = user_query, messages = history)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed time: ", elapsed_time, " seconds")
        return answer.replace("</s>", "") # not useful with the choosen model

