import os
from typing import List, Dict
from math import log10
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class Document:
    def __init__(self, subject: str, content: str, language: str = 'english') -> None:
        self.subject = subject
        self.content = content
        self.language = language
        self.tokens = self._clean_tokens()

    def _clean_tokens(self) -> List[str]:
        """Tokenizes and cleans the content of the document."""
        stop_words = set(stopwords.words(self.language))
        tokens = word_tokenize(self.content)
        return [token.lower() for token in tokens if token.lower() not in stop_words]

    def tf(self, token: str) -> float:
        """Calculates term frequency for a given token."""
        return self.tokens.count(token.lower()) / len(self.tokens)


class Corpus:
    def __init__(self, folder_path: str = None, language: str = 'english') -> None:
        self.documents = []
        self.idf_cache = {}  # Cache to store IDF values
        if folder_path:
            self.read_documents_from_folder(folder_path, language)

    def read_documents_from_folder(self, folder_path: str, language: str = 'english') -> None:
        """Reads documents from the specified folder, creating a Document instance for each file."""
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                subject = filename[:-4]
                with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.documents.append(
                        Document(subject=subject, content=content, language=language))

    def idf(self, token: str) -> float:
        """Calculates inverse document frequency for a given token."""
        if token in self.idf_cache:
            return self.idf_cache[token]

        N = len(self.documents)
        df = sum(1 for doc in self.documents if token.lower() in doc.tokens)
        idf_value = log10(N / (df + 1))
        self.idf_cache[token] = idf_value
        return idf_value

    def tf_idf(self) -> Dict[str, Dict[str, float]]:
        """Calculates TF-IDF scores for all documents in the corpus."""
        corpus_tfidf = {}
        for doc in self.documents:
            doc_tfidf = {token: doc.tf(token) * self.idf(token)
                         for token in set(doc.tokens)}
            corpus_tfidf[doc.subject] = doc_tfidf
        return corpus_tfidf
