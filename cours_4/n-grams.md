corpus = ensemble de documents
document = ensemble de tokens

exemple:

```python
corpus = {
    "doc_1": "Ceci est un exemple de document.",
    "doc_2": "Voici un autre exemple de document.",
    "doc_3": "Et ca aussi c'est un autre type de document."
}

tokens = {
    "doc_1": ["Ceci", "est", "un", "exemple", "de", "document"],
    "doc_2": ["Voici", "un", "autre", "exemple", "de", "document"]
    "doc_3": ["Et", "ca", "aussi", "c'est", "un", "autre", "type", "de", "document"]
}
```

Un N-gram c'est un un groupe de tokens avec N etant le nombre de tokens constitutifs du groupe. Exemple: un bi-gram (ou 2-gram) est un groupe de deux tokens.

N = 1 => Unigram
N = 2 => Bigram
N = 3 => Trigram
N = 4 => Ngram de 4
N = 5 => Ngram de 5
N = n => Ngram de n


Le seul moyen de faire du bon travail est d'aimer ce que vous faites.

unigrams = [Le, seul, moyen, de, faire, du, bon, travail, est, de, aimer, ce, que, vous, faites]

bigrams = [Le seul, moyen de, faire du, bon travail, est de, aimer ce, que vous, faites]