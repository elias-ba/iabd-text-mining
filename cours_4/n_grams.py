from nltk import ngrams

sentence = "Le seul moyen de faire du bon travail est d'aimer ce que vous faites."
n = 3
unigrams = ngrams(sentence.split(), n)
for gram in unigrams:
    print(gram)