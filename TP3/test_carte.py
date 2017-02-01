import unittest

import carte
from carte import *

class TestCreationCarteAvecSoldeEtTicket(unittest.TestCase):
    def test_creer_carte_avec_solde_et_ticket(self):
        c = Carte(42, 42, 7)
        self.assertEqual(42, c.nb_ticket())
        self.assertEqual(42, c.solde())
        self.assertEqual(7, c.prix_ticket())

class TestDebiterSoldeCarte(unittest.TestCase):
    def test_debiter_solde_carte(self):
        c = Carte(42,0,0)
        c.debiter(30)
        self.assertEqual(12, c.solde())

    def test_debiter_solde_valeur_finale_solde_zero(self):
        c = Carte(42,0,0)
        c.debiter(42)
        self.assertEqual(0, c.solde())

    def test_debiter_solde_valeur_negative_erreur(self):
        c = Carte(42,0,0)
        with self.assertRaises(ValueError):
            c.debiter(-10)

    def test_debiter_solde_valeur_zero_erreur(self):
        c = Carte(42,0,0)
        with self.assertRaises(ValueError):
            c.debiter(0)

    def test_debiter_solde_insuffisant_erreur(self):
        c = Carte(1,0,0)
        with self.assertRaises(SoldeInsuffisantError):
            c.debiter(42)
    
    def test_debiter_solde_null_erreur(self):
        c = Carte(0,0,0)
        with self.assertRaises(SoldeInsuffisantError):
            c.debiter(1)

class TestUtiliserTicketCarte(unittest.TestCase):
    def test_utiliser_ticket_carte(self):
        c = Carte(0,10,7)
        c.utiliser_ticket()
        self.assertEqual(9, c.nb_ticket())

    def test_utiliser_ticket_carte_zero_ticket(self):
        c = Carte(0,0,7)
        with self.assertRaises(NbTicketInsuffisantError):
            c.utiliser_ticket()
