from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dl-curriculum.pdf")

doc = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=10,
    separator=''
)

result = splitter.split_documents(doc)

print(result)