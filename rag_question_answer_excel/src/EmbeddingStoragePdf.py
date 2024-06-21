import pandas as pd
import numpy as np
from ModelEmbedding import *
import chromadb
from PdfReader import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb.utils import embedding_functions

ans = "Answers"
emb = "embedding"

class EmbeddingStoragePdf:
    def __init__(
            self, 
            db_name, 
            pdf_reader,
            model_embedding = ModelEmbedding()
    ):
        chroma_client = chromadb.PersistentClient(path=db_name)
        #chroma_client = chromadb.Client()
        sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name = "multi-qa-MiniLM-L6-cos-v1")
        self.db = chroma_client.create_collection(name="pdf", embedding_function = sentence_transformer_ef)
        self.model = model_embedding
        self.pdf_reader = pdf_reader

    def read_data_from_pdf(self):
        files = self.pdf_reader.list();
        rslt = [self.pdf_reader.load_pages(file) for file in files]
        #flatten
        return [item for sublist in rslt for item in sublist]

    def store(self):
        data = self.read_data_from_pdf()
        self.store_data(data)

    def store_data(self, data):
        print(data)
        self.db.add(
            documents = data,
            ids = [str(i) for i in range(0, len(data))]
        )

storage = EmbeddingStoragePdf(
    pdf_reader = PdfReader("../corpus"),
    db_name = "embedding_pdf"
)
storage.store()
