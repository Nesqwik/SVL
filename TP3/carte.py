import caisse
from caisse import SoldeInsuffisantError
from caisse import NbTicketInsuffisantError

class Carte:
    def __init__(self, solde, nb_ticket, prix_ticket):
        '''
        Permet d'instancier une carte avec :
        solde / nombre de tickets / prix du ticket
            >>> c = Carte(42,10,7)
            >>> c.solde()
            42
            >>> c.nb_ticket()
            10
            >>> c.prix_ticket()
            7
        '''
        self.m_solde = solde
        self.m_nb_tickets = nb_ticket
        self.m_prix_ticket = prix_ticket

    def nb_ticket(self):
        '''
        Permet de connaitre le nombre de tickets restants
            >>> c = Carte(42,10,7)
            >>> c.nb_ticket()
            10
        '''
        return self.m_nb_tickets

    def solde(self):
        '''
        Permet de connaire le solde restant
            >>> c = Carte(42,10,7)
            >>> c.solde()
            42
        '''
        return self.m_solde

    def prix_ticket(self):
        '''
        Permet de connaitre le prix d'un ticket
            >>> c = Carte(42,10,7)
            >>> c.prix_ticket()
            7
        '''
        return self.m_prix_ticket

    def debiter(self, amount):
        '''
        Permet de debiter la valeur passee en parametre au solde
            >>> c = Carte(42,10,7)
            >>> c.debiter(10)
            >>> c.solde()
            32
        
        Attention un montant inferieur ou egal a zero provoquera une ValueError
            >>> c = Carte(42,10,7)
            >>> c.debiter(-10)
            Traceback (most recent call last):
            [...]
            ValueError

        Si le solde est inferieur au montant a debiter SoldeInsuffisantError est remonte
            >>> c = Carte(10,10,7)
            >>> c.debiter(50)
            Traceback (most recent call last):
            [...]
            SoldeInsuffisantError
        '''
        if(amount <= 0):
            raise ValueError
        if(self.m_solde < amount):
            raise SoldeInsuffisantError
        self.m_solde -= amount

    def utiliser_ticket(self):
        '''
        Utilise un ticket sur la carte
            >>> c = Carte(10,10,7)
            >>> c.utiliser_ticket()
            >>> c.nb_ticket()
            9

        Si le nombre de tickets est a zero NbTicketInsuffisantError est remonte
            >>> c = Carte(10,0,7)
            >>> c.utiliser_ticket()
            Traceback (most recent call last):
            [...]
            NbTicketInsuffisantError
        '''
        if(self.m_nb_tickets == 0):
            raise NbTicketInsuffisantError
        self.m_nb_tickets -= 1
