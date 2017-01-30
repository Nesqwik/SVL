class Caisse:
    def __init__(self):
        self.carte = None

    def inserer_carte(self, carte):
        self.carte = carte

    def solde(self):
        return self.carte.solde()

    def nb_ticket(self):
        return self.carte.nb_ticket()

    def retirer_carte(self):
        self.check_carte_exists()
        carte = self.carte
        self.carte = None
        return carte

    def payer_repas_avec_ticket(self, amount):
        self.check_carte_exists()
        if(self.carte.nb_ticket() == 0):
            raise NbTicketInsuffisantError
        if(self.carte.prix_ticket() + self.carte.solde() < amount):
            raise SoldeInsuffisantError

        self.carte.utiliser_ticket()
        if(amount > self.carte.prix_ticket()):
            self.carte.debiter(amount - self.carte.prix_ticket())


    def payer_repas_sans_ticket(self, amount):
        self.check_carte_exists()
        if(self.carte.solde() < amount):
            raise SoldeInsuffisantError

        self.carte.debiter(amount)

    def check_carte_exists(self):
        if(self.carte == None):
            raise CarteManquanteError


class CarteManquanteError(Exception):
    pass

class SoldeInsuffisantError(Exception):
    pass

class NbTicketInsuffisantError(Exception):
    pass
