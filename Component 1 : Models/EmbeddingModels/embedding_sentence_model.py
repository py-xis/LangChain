from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = 'New Delhi is the capital of India'

vector = embedding.embed_query(text)
print(vector)
print(str(vector))
