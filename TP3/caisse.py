from carte import Carte

class Caisse:
    def __init__(self):
        '''
        Initialise la caisse avec aucune carte d'insere
            >>> c = Caisse()
            >>> c.retirer_carte()
            Traceback (most recent call last):
            [...]
            CarteManquanteError
        '''
        self.carte = None

    def inserer_carte(self, carte):
        '''
        Insert une carte dans la caisse. Si une carte est deja presente
        Une erreur LecteurDejaUtiliseError est remontee
            >>> c = Caisse ()
            >>> carte = Carte(42,7,7)
            >>> c.inserer_carte(carte)
            >>> c.retirer_carte()
            carte
            >>> c.inserer_carte(carte)
            >>> c.inserer_carte(carte)
            Traceback (most recent call last):
            [...]
            LecteurDejaUtiliseError
        '''
        if(self.carte != None):
            raise LecteurDejaUtiliseError
        self.carte = carte

    def solde(self):
        '''
        Permet de recuper le solde de la carte dans la caisse
            >>> c = Caisse()
            >>> carte = Carte(42,10,7)
            >>> c.inserer_carte(carte)
            >>> c.solde()
            42
        '''
        return self.carte.solde()

    def nb_ticket(self):
        '''
        Permet de recuperer le nombre de tickets de la carte dans la caisse
            >>> c = Caisse()
            >>> carte = Carte(42,12,7)
            >>> c.nb_ticket()
            12
        '''
        return self.carte.nb_ticket()

    def retirer_carte(self):
        '''
        Permet de retirer la carte dans la caisse
        Si il n'y a pas de carte dans la caisse remonte l'erreur:
        CarteManquanteError
            >>> c = Caisse ()
            >>> carte = Carte(42,7,7)
            >>> c.inserer_carte(carte)
            >>> c.retirer_carte()
            carte
            >>> c.retirer_carte()
            Traceback (most recent call last):
            [...]
            CarteManquanteError
        '''
        self.check_carte_exists()
        carte = self.carte
        self.carte = None
        return carte

    def payer_repas_avec_ticket(self, amount):
        '''
        Paye un repas en utilisant en priorite l'agent contenu sur les tickets
        N'utilise qu'un seul ticket par payement
        Controle si une carte est presente si non remonte CarteManquanteError
            >>> c = Caisse()
            >>> carte = Carte(40,10,7)
            >>> c.inserer_carte(carte)
            >>> c.payer_repas_avec_ticket(10)
            >>> c.solde()
            37
            >>> c.nb_ticket()
            9
        
        Controle si le nombre de ticket est suffisant si non remonte une erreur:
        NbTicketInsuffisantError
        Controle si le solde est suffisant si non remonte une erreur:
        SoldeInsuffisantError
        '''
        self.check_carte_exists()
        if(self.carte.nb_ticket() == 0):
            raise NbTicketInsuffisantError
        if(self.carte.prix_ticket() + self.carte.solde() < amount):
            raise SoldeInsuffisantError

        self.carte.utiliser_ticket()
        if(amount > self.carte.prix_ticket()):
            self.carte.debiter(amount - self.carte.prix_ticket())


    def payer_repas_sans_ticket(self, amount):
        '''
        Paye un repas seulement avec le solde de la carte
            >>> c = Caise()
            >>> carte = Carte(42,10,7)
            >>> c.inserer_carte(carte)
            >>> c.payer_repas_sans_ticket(22)
            >>> c.solde()
            20
            >>> c.nb_ticket()
            10

        Si le solde est insuffisant remonte une SoldeInsuffisantError
        '''
        self.check_carte_exists()
        if(self.carte.solde() < amount):
            raise SoldeInsuffisantError

        self.carte.debiter(amount)

    def check_carte_exists(self):
        if(self.carte == None):
            raise CarteManquanteError


class LecteurDejaUtiliseError(Exception):
    pass

class CarteManquanteError(Exception):
    pass

class SoldeInsuffisantError(Exception):
    pass

class NbTicketInsuffisantError(Exception):
    pass
