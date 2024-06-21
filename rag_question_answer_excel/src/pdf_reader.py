from langchain_text_splitters import RecursiveCharacterTextSplitter
from PdfReader import PdfReader

file_path = "../corpus"
reader = PdfReader(file_path)
files = reader.list()
file = files[0]
pages = reader.load_pages(file)
page = pages[0]
print()
print(page)