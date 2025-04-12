from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv("../.env")

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "My laptop is an Apple Macbook Air M2",
    "My Phone is a Samsung Galaxy F34 5G",
    "My Tablet is a Samsung Galaxy Tab S9"
]

result = embedding.embed_documents(documents)
print(result)
print(str(result))