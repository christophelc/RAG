from langchain_community.document_loaders import PyPDFLoader
import os
import glob

class PdfReader:
    def __init__(self, path):
        self.path = path

    def list(self):
        files = glob.glob(self.path + "/*.pdf")
        return files
    
    def load_pages(self, file_path):
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        return [page.page_content for page in pages]
    