TFIDF est un algo. Il est beaucoup utilise dans le domaine du information retrieval (text mining). Le but de l'algo est d'accorder un certain score aux mots dans un document en calculant le rapport entre la frequence des mots dans le document et leurs frequences dans le corpus.

TFIDF((m,d)/c) = score d'importance

L'idee de l'algo c'est de calculer les TFIDF de tous les mots d'un document / corpus et de les classifier du plus grand au plus petit. Les N mots les plus grands donnent le sens / la classe / le theme du document.

Il y a des manifestations a Dakar aujourd'hui. Ces manifestations ont commence depuis 2021.

P(Il) = 1/14
P(manifestations) = 2/14

TF est une methode de calcul de la frequence d'un mot donne dans un document. On va noter TF(m, d). Le resultat de TF depend fortement de la taille du document et du carractere generale ou specifique du mot. Exemple le TF des articles le, la, les, etc est forcement toujours grand car ces mots sont naturellement tres frequent dans la langue francaise. Et plus le document est long plus on a la chance de les retrouver. Souvent pour eviter que ces mots ne fausse nos calculs, on les enleve du document. Ces mots sont souvent appelle des 'stopwords'.

- On a un document D1 qui fait 100 mots avec 40 fois le mot 'manifestations'
- On a un autre document D2 qui fait 1000 mots avec 237 fois le mot 'manifestations'

```
TF(m, d) = nombre d'occurence du mot m dans le document d / nombre de mots dans le document d
```

```
DF(m, c) = nombre de documents du corpus c dans lesquels le mot m apparait / nombre total de document dans le corpus
```

```python
corpus = {
    "doc_1": "Il y a des manifestations aujourd'hui a Dakar",
    "doc_2": "Ces manifestations ont commence depuis 2021",
    "doc_3": "Cette situation affecte trop la stabilite du pays",
    "doc_4": "Le Senegal n'a jamais connu autant de manifestations en si peu de temps",
    "doc_5": "Tout le monde en souffre"
}

TF("manifestations", "doc_1") = 1 / 5
TF("manifestations", "doc_2") = 1 / 4
TF("manifestations", "doc_3") = 0 / 3
TF("manifestations", "doc_4") = 1 / 9
TF("manifestations", "doc_5") = 0 / 5

DF("manifestations", corpus) = 3
```

```
NDF = DF / N avec N etant le nombre de doc dans le corpus
IDF = 1/NDF = N/DF
```

IDF = log(N/(df + 1))

```
TFxIDF = tf(m, d) * log(N/(df + 1)) 
avec m etant le mot, d etant le document courant, N etant la taille du corpus, et df etant le nombre de document dans lesquels le mot m apparait dans tout le corpus.
```