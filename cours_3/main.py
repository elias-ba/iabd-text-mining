# TFxIDF = tf(m, d) * log(N/(df + 1))

from typing import List
from math import log10


class Doc:
    def __init__(self, subject: str, content: str) -> None:
        self.subject = subject
        self.content = self.clean(content)
        self.words = self.content.split()

    def __repr__(self) -> str:
        return f"{self.subject}\n{self.content}"

    def clean(self, text: str) -> str:
        to_clean = (",", ".")
        for char in to_clean:
            text = text.replace(char, "")
        return text

    def tf(self, word: str) -> float:
        return sum(1 for w in self.words if word.lower()
                   == w.lower()) / len(self.words)

    def tf_idf(self, word: str, idf: float) -> float:
        return self.tf(word) * idf


def idf(corpus: List[Doc], word: str) -> int:
    # log(N/(df + 1))
    N = len(corpus)
    df = sum(1 for doc in corpus if word.lower() in doc.content.lower())
    return log10(N/(df + 1))


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
    """),
    Doc(subject="Commerce", content="""
        La est un aspect fondamental de la qualité de vie. Les avancées médicales 
        ont permis de combattre de nombreuses maladies, mais des défis subsistent, 
        comme l'émergence de maladies non transmissibles liées au mode de vie. 
        Une alimentation équilibrée, une activité physique régulière et un suivi médical 
        sont essentiels pour maintenir une bonne santé.
    """)
]

word = "santé"

idf = idf(corpus, word)

print(f"Le df de '{word}' est de {idf}")

print("----------------------------------------")

for doc in corpus:
    tf_idf = doc.tf_idf(word, idf)
    print(f"Le TF-IDF de '{word}' dans le document '{
          doc.subject}' est de {tf_idf}")
