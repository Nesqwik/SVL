# TP5 - Exercice 1

import datetime

class Emprunt:
    def __init__(self, utilisateur, livre):
        self.utilisateur = utilisateur
        self.livre = livre
        self.date_emprunt = datetime.date.today()

    def get_livre(self):
        return self.livre

    def get_utilisateur(self):
        return self.utilisateur

    def get_date_emprunt(self):
        return self.date_emprunt

    def est_en_retard(self):
        delta = datetime.date.today() - self.date_emprunt
        return delta.days > 30
