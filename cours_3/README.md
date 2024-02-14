
# TF-IDF Implementation

## Description

Term Frequency-Inverse Document Frequency (TF-IDF) is a statistical measure used to evaluate the importance of a word in a document relative to a collection of documents, known as a corpus. Originating from the field of information retrieval and text mining, TF-IDF serves to highlight words that are more interesting, i.e., frequent in a specific document but rare across multiple documents. This technique is widely utilized in various applications, including search engines, document clustering, and text classification, to assess and rank documents' relevance concerning user queries.

### Purpose

The primary purpose of TF-IDF is to identify the significance of words within documents of a corpus. By diminishing the weight of commonly used words across all documents (stopwords) and increasing the weight of terms significant to a specific document, TF-IDF allows for efficient information retrieval and knowledge discovery.

### History

The concept of TF-IDF was developed during the 1970s as a response to the needs of document retrieval and text mining. It has since become a foundational tool in the field of natural language processing (NLP), enabling the indexing and ranking of documents based on their relevance to specific terms.

### How It Works

TF-IDF combines two metrics: Term Frequency (TF) and Inverse Document Frequency (IDF).

- **Term Frequency (TF)** calculates the frequency of a word in a given document, indicating the importance of the term within that specific document.

    ```math
    TF(m, d) = (Number of times term m appears in a document d) / (Total number of terms in the document d)
    ```

- **Inverse Document Frequency (IDF)** assesses the general importance of the term across a corpus.

    ```math
    IDF(m, c) = log(Total number of documents in the corpus c / Number of documents containing term m)
    ```

- **TF-IDF Score**: The TF-IDF value increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the corpus.

    ```math
    TF-IDF(m, d, c) = TF(m, d) * IDF(m, c)
    ```

## Implementation Details

This repository contains a Python implementation of the TF-IDF algorithm from scratch. The implementation is structured around two main classes: `Document` and `Corpus`, facilitating the calculation of TF, IDF, and TF-IDF scores for a given set of documents.

### Features

- Tokenization and cleaning of text documents.
- Calculation of term frequencies within documents.
- Computation of inverse document frequency across the corpus.
- Ranking of terms within documents based on TF-IDF scores.

## How to Test

To test the TF-IDF implementation with your documents:

1. **Prepare Your Documents**: Place your text documents within a designated folder. Each document should be in a separate text file.

2. **Configure the Corpus**: Utilize the `Corpus` class to read documents from the folder and preprocess them.

    ```python
    from tfidf import Corpus

    corpus = Corpus(folder_path='path/to/your/documents', language='english')
    ```

3. **Calculate TF-IDF Scores**: Invoke the `tf_idf` method to calculate and display the TF-IDF scores for terms within your documents.

    ```python
    tf_idf_scores = corpus.tf_idf()
    print(tf_idf_scores)
    ```

4. **Analyze Results**: The output will include TF-IDF scores for each term within each document, allowing you to analyze the importance and relevance of terms across your corpus.

## Contributing

Contributions to improve the implementation or extend its functionality are welcome. Please feel free to fork the repository, make changes, and submit pull requests.
