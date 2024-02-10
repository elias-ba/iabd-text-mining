# Exercice

Ecrire un programme Python qui permet de lire un texte qui contient des numeros de telephones et qui extrait ces numeros dans une base de connaissance en utilisant une expression reguliere avec des groupes de captures. Les numeros sont toujours au format +xxx yy aaa bb cc. +xxx represente l'indicatif du pays, il est possible d'avoir des numeros sans indicatifs. yy est le code de l'operateur, 77 pour Orange, 76 pour Free, 70 pour Expresso, 60 pour MTN, et 50 pour Vodacom. aaa bb cc forme le numeros en tant que tel. Le programme doit extraire les differents groupes que sont: indicatif, code_operateur, et numero.

1. D'abord ecrire l'expression reguliere et la tester sur [regex101.com](https://regex101.com/)
2. Ecrire le programme Python qui utilise cette regex pour effectuer l'extraction