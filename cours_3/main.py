# TFxIDF = tf(m, d) * log(N/(df + 1))

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from typing import List
from math import log10
import nltk

nltk.download('stopwords')
nltk.download('punkt')


class Doc:
    def __init__(self, subject: str, content: str) -> None:
        self.subject = subject
        self.content = content
        self.tokens = word_tokenize(self.content)
        stop_words = set(stopwords.words('french'))
        self.clean_tokens = [
            token.lower() for token in self.tokens if token.lower() not in stop_words]
        self.tf_idfs = {}

    def __repr__(self) -> str:
        return f"{self.subject}\n{self.content}"

    def tf(self, token: str) -> float:
        return sum(1 for clean_token in self.clean_tokens if clean_token.lower()
                   == token.lower()) / len(self.clean_tokens)


def idf(corpus: List[Doc], token: str) -> int:
    N = len(corpus)
    df = sum(1 for doc in corpus if token.lower() in doc.clean_tokens)
    return log10(N/(df + 1))


def tf_idf(corpus: List[Doc]) -> float:
    for doc in corpus:
        for token in doc.clean_tokens:
            doc.tf_idfs[token] = doc.tf(token) * idf(corpus, token)


corpus = [
    Doc(subject="Technologie", content="""
        La technologie moderne a révolutionné notre façon de vivre et de travailler. 
        L'essor des smartphones, des ordinateurs portables et de l'internet a rendu 
        l'information plus accessible que jamais. Les progrès dans le domaine de 
        l'intelligence artificielle et de la robotique promettent de transformer encore 
        davantage nos vies dans les années à venir. Cependant, cette évolution rapide 
        présente également des défis, notamment en termes de sécurité des données et 
        d'impact sur l'emploi.
    """),
    Doc(subject="Environnement", content="""
        L'environnement naturel est sous pression en raison de l'activité humaine.
        La déforestation, la pollution de l'air et de l'eau, et le changement climatique 
        sont des menaces majeures pour la biodiversité et la survie humaine. 
        Des actions urgentes sont nécessaires pour réduire notre empreinte carbone, 
        protéger les espaces naturels et promouvoir des pratiques durables.
    """),
    Doc(subject="Santé", content="""
        La santé est un aspect fondamental de la qualité de vie. Les avancées médicales 
        ont permis de combattre de nombreuses maladies, mais des défis subsistent, 
        comme l'émergence de maladies non transmissibles liées au mode de vie. 
        Une alimentation équilibrée, une activité physique régulière et un suivi médical 
        sont essentiels pour maintenir une bonne santé.
    """)
]


def get_top(scores: dict, k=5) -> dict:
    return dict(sorted(scores.items(), key=lambda item: item[1], reverse=True)[:k])


tf_idf(corpus)

for doc in corpus:
    top = get_top(doc.tf_idfs)
    print(f"Les 5 mots les plus specifiques au document '{
          doc.subject}' sont: {list(top.keys())}")
