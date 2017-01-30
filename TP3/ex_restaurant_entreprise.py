# demo SVL - CTD3 - 1617 - M. Nebut
# test des interactions avec mockito

class Caisse:

    def __init__(self):
        self.carte = None

    def inserer(self, carte):
        self.carte = carte

    def solde(self):
        if self.carte == None:
            raise CarteManquanteError()
        return self.carte.solde()

    def payer_repas_sans_ticket(self, montant_repas):
        self.carte.debiter(montant_repas)

class CarteManquanteError(Exception):
    pass

class SoldeInsuffisantError(Exception):
    pass
