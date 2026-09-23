# Sentence Embeddings and Semantic Similarity

## Description

This project demonstrates sentence embeddings and semantic similarity using Python.

The `all-MiniLM-L6-v2` model converts sentences into numerical vectors called embeddings. Cosine similarity is then used to find sentences with similar meanings.

## Technologies Used

* Python
* Sentence Transformers
* Scikit-learn
* Cosine Similarity

## Project Structure

```text
embedding/
│
├── embeddingapp.py
└── README.md
```

## Installation

Install the required libraries:

```bash
pip install sentence-transformers scikit-learn
```

## Run the Project

Open the terminal inside the `embedding` folder and run:

```bash
python embeddingapp.py
```

## Features

* Converts sentences into embeddings
* Displays embedding dimensions
* Calculates cosine similarity
* Finds semantically similar sentences
* Displays similarity scores

## Model Used

```text
all-MiniLM-L6-v2
```

## Output

The program displays:

* Total number of sentences
* Embedding dimension
* Sentence embeddings
* Similar sentence pairs
* Cosine similarity scores

## Purpose

The purpose of this project is to understand how sentence embeddings and semantic similarity are used in Natural Language Processing (NLP).
