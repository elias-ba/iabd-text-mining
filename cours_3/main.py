from typing import List, Dict
from math import log10
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
nltk.download('punkt')

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
    def __init__(self, documents: List[Document]) -> None:
        self.documents = documents
        self.idf_cache = {}  # Cache to store IDF values

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
            doc_tfidf = {token: doc.tf(token) * self.idf(token) for token in set(doc.tokens)}
            corpus_tfidf[doc.subject] = doc_tfidf
        return corpus_tfidf

def main():
    # Example Documents
    documents = [
        Document(
            subject="Technologie",
            content="""La technologie moderne a révolutionné notre façon de vivre et de travailler. ...""",
            language='french'
        ),
        Document(
            subject="Environnement",
            content="""L'environnement naturel est sous pression en raison de l'activité humaine. ...""",
            language='french'
        ),
        # Add more documents as needed
    ]

    corpus = Corpus(documents)
    corpus_tfidf = corpus.tf_idf()

    for subject, tfidf_scores in corpus_tfidf.items():
        top_tfidf = dict(sorted(tfidf_scores.items(), key=lambda item: item[1], reverse=True)[:5])
        print(f"Top 5 specific words for '{subject}': {list(top_tfidf.keys())}")

if __name__ == "__main__":
    main()
