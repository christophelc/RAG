from sentence_transformers import CrossEncoder
import torch
import torch.nn.functional as F

class Reranking:
    def __init__(self):
        self.cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

    def predict(self, cross_inp):
        scores = self.cross_encoder.predict(cross_inp)
        return F.softmax(torch.tensor(scores))

# test
cross_encoder = Reranking()
result = cross_encoder.predict([("What is a game ?", "chess is a game")])
model = CrossEncoder('cross-encoder/stsb-TinyBERT-L-4')
scores = model.predict([("The weather today is beautiful", "It's raining"),
                        ("The weather today is beautiful", "Today is a sunny day")])
print(scores)
