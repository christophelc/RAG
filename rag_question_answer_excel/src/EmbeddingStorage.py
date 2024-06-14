import requests
import json
import pandas as pd
import numpy as np
from tinydb import TinyDB
from ModelEmbedding import *

q = "Questions"
ans = "Answers"
emb = "embedding"

class EmbeddingStorage:
    def __init__(self, db_name, model_embedding = ModelEmbedding()):
        self.db = TinyDB(db_name)
        self.model = model_embedding

    #better than csv when cells with line feed inside
    def read_data_from_excel(self, data_path):
        df = pd.read_excel(data_path, sheet_name = "Feuill1")
        #print(df.iloc[0:, 0:3])
        #for idx, item in enumerate(df.iloc[0:, 0:3].to_dict(orient="records"))
        #  print(idx, item)
        #print("xxxxx")
        #print(df.iloc[0:, 0:3].dropna())
        return df.iloc[0:, 0:3].dropna().to_dict(orient='record')

    #ok for cells with no line feeds inside
    def read_data_from_csv(self, data_path):
        df = pd.read_csv(data_path, sep=',', quotechar='"', header=0)
        print(df.iloc[1:, 0:3].dropna())
        return df.iloc[1:, 0:3].dropna().to_dict(orient='records')

    def embedding(self, text_arr):
        return self.model.encode(text_arr)

    def store(self, data_path = "../corpus/data.csv"):
        #data = self.read_data_from_excel(data_path = data_path)
        data = self.read_data_from_csv(data_path = data_path)
        arr=[]
        for item in data:
            print(item)
            arr.append([item[q], item[ans]])
        self.store_data(arr)

    def store_data(self, data):
        corpus_embeddings = self.embedding(data)
        for (q_a, embedding) in zip(data, corpus_embeddings):
            [question, answer] = q_a
            to_add = {
                    q: question,
                    ans: answer,
                    #no nvidia
                    emb: embedding.cpu().data.numpy().tolist()
            }
            self.db.insert(to_add)

storage = EmbeddingStorage(db_name = "data_embedding.json")
storage.store()
