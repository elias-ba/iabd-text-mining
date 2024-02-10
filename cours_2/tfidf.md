# Term Frequency - Inverse Document Frequency (TF-IDF)

## Rappels

- Un corpus est un ensemble de document. Son equivalent est le dataset en data science
- Un document est un ensemble de texte. Son equivalent est un dataframe dans un dataset
- Un texte est la plus petite unite d'observation en text mining. Son equivalent c'est une ligne dans un dataframe

- Un texte contient un ensemble de mots; Qui ne nous interesse que sous leurs formes tokeniser.

- La forme tokeniser d'un texte est la forme qui permet de decouper le texte en plusieurs mots qui le constitue.
  Exemple:

```python
text = "le prof est encore en retard."
tokens = ["le", "prof", "est", "encore", "en", "retard"]
```

- Pour chaque token d'un texte on a parfois besoin de le stemmiser.

- La stemmisation est le fait de ramener un mot a son 'radical'.

Exemple:

```python
mot_1 = "Marcher"
mot_2 = "Marchons"

stem = "Marche"
```

- La lemmatization est le procede qui permet dans un dictionnaire donne, de trouver l'ensemble des 'synonymes' d'un mot.

Exemple:

```python
mot = "voiture"
lem_1 = "bagnole"
lem_2 = "vehicule"
lem_2 = "caisse"
```

Text 1:

Bonjour, je m'appelle Elias, je suis ingenieur logiciel, je travaille chez OpenFn.
J'enseigne aussi. J'habite Saly. En tant qu'ingenieur, je suis souvent confronte a des problemes assez difficile a resoudre. Ce qui rend mon travail assez stressant. Nous utilisons des procedes d'ingenierie assez efficace pour eviter au maximum des erreurs dans les produits que nous concevons.
