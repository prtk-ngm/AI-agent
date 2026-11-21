from openai import OpenAI

client = OpenAI(base_url= "http://localhost:11434/v1", api_key="ollama")

def create_embedding(content):
    response = client.embeddings.create(model="nomic-embed-text", input=content)
    return response.data[0].embedding

