text = """
Bonjour, je m'appelle Elias, je suis ingenieur logiciel, 
je travaille chez OpenFn.
J'enseigne aussi. J'habite Saly. 
En tant qu'ingenieur, je suis souvent confronte a des problemes 
assez difficile a resoudre. Ce qui rend mon travail assez stressant. 
Nous utilisons des procedes d'ingenierie assez efficace pour eviter 
au maximum des erreurs dans les produits que nous concevons.
"""

tokens = text.split(" ")
print(tokens)

TF
Token                    Occurence
Ingenieur                3
Prof                     1
Animateur                4

DF
Token

TF * 1/DF = 