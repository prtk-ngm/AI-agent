from openai import OpenAI
from simlarity import cosine_simlarity

input_1 = "Python is programming langauge"
input_2 = "Pizza is delicious"

client = OpenAI(base_url= "http://localhost:11434/v1", api_key="ollama")
response_1 = client.embeddings.create(model="nomic-embed-text", input=input_1)
response_2 = client.embeddings.create(model="nomic-embed-text", input=input_2)

embedding_1 = response_1.data[0].embedding
embedding_2 = response_2.data[0].embedding


print("len",len(embedding_1))

print("len",len(embedding_2))

print(cosine_simlarity(embedding_1, embedding_2))


