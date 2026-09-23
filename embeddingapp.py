from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


sentences = [
    "I enjoy playing football.",
    "I love playing soccer.",
    "I like eating pizza.",
    "I enjoy cooking delicious food.",
    "Artificial intelligence is changing technology.",
    "AI is used in many modern applications.",
    "Python is easy to learn.",
    "Java is a popular programming language."
]


embeddings = model.encode(sentences)

print("Total number of sentences:", len(sentences))
print("Embedding dimension:", len(embeddings[0]))

# Display embeddings
print("\n--- Embeddings ---")

for i, sentence in enumerate(sentences):
    print("\nSentence:", sentence)
    print("Embedding:", embeddings[i])


similarity = cosine_similarity(embeddings)


print("\n--- Semantic Similarity ---")

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        if similarity[i][j] > 0.5:
            print(
                f"\nSentence 1: {sentences[i]}"
                f"\nSentence 2: {sentences[j]}"
                f"\nSimilarity: {similarity[i][j]:.4f}"
            )