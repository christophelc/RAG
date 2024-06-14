from ModelEmbedding import ModelEmbedding
from transformers import AutoModelForCausalLM, AutoTokenizer
from SimilarityFinder import *

class AnswerGenerator:
    def __init__(
            self,
            db_name,
            model_embedding,
            cross_encoder,
            accuracy,
            rag_top_n,
            rerank_accuracy,
            max_token,
            llm_proxy):
        self.db_name = db_name
        self.accuracy = accuracy
        self.max_token = max_token
        self.rag_top_n = rag_top_n
        self.rerank_accuracy = rerank_accuracy
        self.llm_proxy = llm_proxy
        self.cross_encoder = cross_encoder
        self.similarity_finder = SimilarityFinder(
                db_name = db_name,
                model_embedding = model_embedding
        )
        self.msg_empty = "Please ask question about your specialization"

    def semantic_search(self, query):
        top = self.similarity_finder.semantic_search(query, self.rag_top_n, self.accuracy)
        return top

    def build_context(self, query):
        answers = self.semantic_search(query = query)
        if len(answers) > 0:
            #reranking results
            cross_inp = [(query, answer) for answer in answers[:self.rag_top_n]]
            cross_scores = self.cross_encoder.predict(cross_inp)
            answers_score_sorted = sorted(list(zip(answers, cross_scores)), key = lambda x: -x[1])
            print(answers_score_sorted)
            answers = [answer for [answer, score] in answers_score_sorted if score >=self.rerank_accuracy]
        return answers
    
    def remove_out_of_scope(self, messages):
        filtered_messages=[]
        ignore_previous = False

        for i in range(len(messages) -1, -1, -1):
            if ignore_previous:
                ignore_previous = False
                continue
            if messages[i].get('role') == 'assistant' and messages[i].get('content') == self.msg_empty:
                ignore_previous = True
            else:
                filtered_messages.insert(0, messages[i])

        return filtered_messages

    def call_llm(self, user_query, messages, context_text):
        print("-- context --")
        print(context_text)
        print("-------------")
        user_message = {"role": "user", "content" : user_query }
        #remove system content that are just old clues
        messages_wt_old = [messages[0]] + [message for message in messages[1:] if message.get('role') != 'system']
        messages_scope = self.remove_out_of_scope(messages_wt_old)
        if context_text != "":
            system_message = {"role": "system", "content": "The knowledge base is:\n" + context_text}
            messages_scope.append(system_message)
        messages_scope.append(user_message)
        print(messages_scope)
        print("---------------")
        generated_text = self.llm_proxy.call_llm(messages_scope)
        return generated_text

    def build_answer(self, user_query, messages):
        best_answers = self.build_context(query = user_query)
        if (len(best_answers) == 0):
            return self.msg_empty
        else:
            context_text = " kw: " + "\n kw: ".join(best_answers)
            generated_text = self.call_llm(
                    user_query,
                    messages,
                    context_text)
            return generated_text

    #for llm launched with internal call (python) => not useful 
    def extraction_assistant_answer(self, answer):
        assistant = "<|assistant|>"
        lines = answer.split("\n")
        try:
            idx = lines.index(assistant)
            if (idx >= 0):
                return "\n".join(lines[idx+1:])
            else:
                return ""
        except:
            return answer

    def run(self, user_query, messages):
        answer = self.build_answer(user_query = user_query, messages = messages)
        return self.extraction_assistant_answer(answer)
