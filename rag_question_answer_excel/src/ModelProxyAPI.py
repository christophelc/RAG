from operator import ge
from openai import OpenAI

class ModelProxyAPI:
    def __init__(self):
        self.client = OpenAI(
                base_url="http://localhost:8080/v1", 
                api_key = "sk-no-key-required")
        self.model="LLaMA_CPP"

    def call_llm(self, messages):
        completion = self.client.chat.completions.create(
                model = self.model,
                messages = messages,
                temperature = 0.2)
        response = completion.choices[0].message
        return response.content
