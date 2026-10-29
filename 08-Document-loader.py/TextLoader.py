from langchain_community.document_loaders import TextLoader # type: ignore

loader = TextLoader("cricket.txt", encoding= "UTF-8")

result = loader.load()

print(result[0].page_content)
print(result[0].metadata)