# SVL 16-17 - M. Nebut
# TP property-based testing avec Hypothesis
# une version fausse du compte avec découvert

class Compte:

    def __init__(self):
        self.montant = 0.0
        self.decouvert_autorise = False
        self.decouvert = None
        
    def crediter(self, somme):
        """
        pre:
           somme > 0.0
        post[self.montant]:
           self.montant == __old__(self.montant) + somme
        """
        if somme <= 0:
            raise ValueError("la somme doit etre strictement positive")
        self.montant += somme

    def debiter(self, somme):
        """
        pre:
           somme > 0.0
        post[self.montant]:
           self.montant == __old__(self.montant) - somme
        """
        if somme <= 0:
            raise ValueError("la somme doit être positive")
        if self.decouvert_autorise and self.montant - somme < self.decouvert:
            raise ValueError("la somme débitee ne doit pas faire excéder le découvert")
        if not self.decouvert_autorise and self.montant - somme < 0:
            raise ValueError("la somme débitée ne doit pas passer le solde en négatif")
        self.montant -= somme

    def autoriser_decouvert(self, decouvert):
        """
        pre:
            decouvert < 0.0
        """
        if decouvert >= 0:
            raise ValueError("le découvert doit être négatif")
        self.decouvert_autorise = True
        self.decouvert = decouvert
