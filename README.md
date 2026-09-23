# Sentence Embeddings and Semantic Similarity

## Description

This project demonstrates how to convert sentences into numerical vectors called **embeddings** and measure the semantic similarity between sentences using **Cosine Similarity**.

The project uses the `all-MiniLM-L6-v2` model from Sentence Transformers.

## Technologies Used

* Python
* Sentence Transformers
* Scikit-learn
* Cosine Similarity

## How It Works

1. Load the `all-MiniLM-L6-v2` Sentence Transformer model.
2. Store multiple sentences in a list.
3. Convert each sentence into an embedding.
4. Calculate cosine similarity between all sentence embeddings.
5. Display sentence pairs with similarity greater than `0.5`.

## Example Sentences

* I enjoy playing football.
* I love playing soccer.
* Artificial intelligence is changing technology.
* AI is used in many modern applications.
* Python is easy to learn.
* Java is a popular programming language.

## Installation

Install the required libraries:

```bash
pip install sentence-transformers scikit-learn
```

## Run the Project

Save the Python file as:

```text
embeddings.py
```

Run it using:

```bash
python embeddings.py
```

## Output

The program displays:

* Total number of sentences
* Embedding dimension
* Embeddings for each sentence
* Semantically similar sentence pairs
* Cosine similarity score

## Purpose

The purpose of this project is to understand how **sentence embeddings** and **semantic similarity** are used in Natural Language Processing (NLP).

## Conclusion

Sentence embeddings represent the meaning of sentences as numerical vectors. Cosine similarity can then be used to identify sentences that have similar meanings even when they use different words.
