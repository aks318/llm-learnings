import wikipedia

from langchain_community.retrievers import WikipediaRetriever

wikipedia.set_user_agent(
    "AILearningProject/1.0 (personal learning project)"
)

retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = "Why virat is best in test"

docs = retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}...")  # truncate for display