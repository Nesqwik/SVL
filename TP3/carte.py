class Carte:
    def __init__(self, solde, nb_ticket, prix_ticket):
        self.m_solde = solde
        self.m_nb_tickets = nb_ticket
        self.m_prix_ticket = prix_ticket

    def nb_ticket(self):
        return self.m_nb_tickets

    def solde(self):
        return self.m_solde

    def prix_ticket(self):
        return self.m_prix_ticket
