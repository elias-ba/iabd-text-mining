import re

pattern = r'(?P<username>[A-Za-z0-9.]+)@(?P<service>[A-Za-z0-9]+)\.(?P<domain>(?P<subdomain_1>[A-Za-z0-9]+)(?P<subdomain_2>\.[A-Za-z0-9]+)?)'

text = """
Jean Dupont, email: jean.dupont@email.com, téléphone: 06 12 34 56 78. Marie-Claire Estier, email: marie.estier@exemple.fr, téléphone: 07 65 43 21 00. Réunion prévue le 25/03/2024 à Paris, suivie d'un second rendez-vous le 12/04/2024 à Lyon.
mamadou.ka@esp.edu.sn
Liste de tâches à accomplir :

Envoyer la documentation technique à tech.docs@entreprise.com avant le 30/04/2024.
Confirmer la réservation de la salle de conférence pour le 05/05/2024.
Contacter M. Lemoine au 01 23 45 67 89 concernant le dossier en cours.
Notes diverses :

Le code de projet est REF-2024-XL89.
L'adresse IP du serveur principal est 192.168.1.1.
Visiter le site www.exemple-website.com pour plus d'informations.
"""

match = re.search(pattern, text)

if match:
    username = match.group('username')
    service = match.group('service')
    domain = match.group('domain')

    print(username)
    print(service)
    print(domain)
else:
    print("Aucune adresse email trouvee dans le texte")
