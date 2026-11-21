from simlarity import cosine_simlarity
from embeddings import create_embedding

def semantic_search(query,
    chunks,
    top_k=5):

    query_embedding = create_embedding(query)
    results = []
    for chunk in chunks:
        similarity_score = cosine_simlarity(query_embedding, chunk["embedding"])
        results.append({"text": chunk["text"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "semantic_score": similarity_score})

    results.sort(key=lambda item: item["semantic_score"], reverse=True)
    return results[:top_k]



def keyword_score(query, text):
    query_words = set(
        query.lower().split()
    )
    text_words = set(
        text.lower().split()
    )
    if not query_words:
        return 0.0

    matches = (
        query_words
        &
        text_words
    )
    return len(matches) / len(
        query_words
    )

def hybrid_search(
    query,
    chunks,
    top_k=5,
    semantic_weight=0.7,
    keyword_weight=0.3
):
    query_embedding = create_embedding(
        query
    )

    for chunk in chunks:
        semantic_score = cosine_simlarity(query_embedding, chunk["embedding"])
        keyword_score = keyword_score(query, chunk["text"])
        combined_score = semantic_weight * semantic_score + keyword_score * keyword_weight
        results.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "semantic_score": semantic_score,
            "keyword_score": keyword_score,
            "combined_score": combined_score
        })

    results = []

    results.sort(
        key=lambda item:
        item["combined_score"],
        reverse=True
    )

    return results[:top_k]



