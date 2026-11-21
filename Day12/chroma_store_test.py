from retriever import semantic_search
from embeddings import create_embedding, embed_chunks
from chroma_store import add_chunks, search

chunks = [{
    "text": "Python is a programming language",
    "source": "source1.txt",
    "chunk_id": "01",
    "semantic_score": "0.9",
    "embedding": create_embedding("Python is a programming language")
        
}, 
{
    "text": "Java is a programming language",
    "source": "source2.txt",
    "chunk_id": "02",
    "semantic_score": "0.5",
    "embedding": create_embedding("Java is a programming language")

}]


add_chunks(embed_chunks(chunks=chunks))

print(search(create_embedding("Python is a programming language"), top_k=2))