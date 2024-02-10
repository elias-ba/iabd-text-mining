# TFxIDF = tf(m, d) * log(N/(df + 1))

class Doc:
    def __init__(self, subject, content):
        self.subject = subject
        self.content = self.clean(content)

    def __repr__(self):
        return f"{self.subject}\n{self.content}"

    def clean(self, text):
        to_clean = [",", "."]
        for char in to_clean:
            text = text.replace(char, "")
        return text

    def tf(self, mot):
        # print(f"Le mot est: {mot}")
        words = self.content.split()
        # print(f"Les mots du text sont: {words}")
        self.frequency = sum(
            [1 for word in words if word.lower() == mot.lower()])


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

mot = "de"

for doc in corpus:
    doc.tf(mot)

for doc in corpus:
    print(f"Le TF de {mot} dans le document '{
          doc.subject}' est de {doc.frequency}")
