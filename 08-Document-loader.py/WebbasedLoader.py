from langchain_community.document_loaders import WebBaseLoader

url = "https://ollama.com/library/qwen3-coder:30b"

loader = WebBaseLoader(url)

doc = loader.load()

print(doc[0].page_content)