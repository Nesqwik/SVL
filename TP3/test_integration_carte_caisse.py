import unittest
from mockito import mock, when, verify

import caisse
import carte
from caisse import *
from carte import *

class TestIntegrationLaCarteEstInsereeEtRetireeDeLaCaisse(unittest.TestCase):
    def test_inserer_retirer_carte(self):
        caisse = Caisse()
        carte = Carte(42,7,7)

        caisse.inserer_carte(carte)

        self.assertEqual(carte, caisse.retirer_carte())

    def test_inserer_carte_avec_carte_deja_insere(self):
        caisse = Caisse()
        carte = Carte(42,7,7)
        carte2 = Carte(42,7,7)

        caisse.inserer_carte(carte)
        with self.assertRaises(LecteurDejaUtiliseError):
            caisse.inserer_carte(carte2)

    def test_retirer_carte_sans_inserer(self):
        caisse = Caisse()

        with self.assertRaises(CarteManquanteError):
            caisse.retirer_carte()



class TestIntegrationLaCaisseVisualiseLesSoldesDeLaCarte(unittest.TestCase):

    def test_visualiser_solde_carte(self):
        caisse = Caisse()
        carte = Carte(42,7,7)

        caisse.inserer_carte(carte)
        self.assertEqual(42, caisse.solde())

    def test_visualiser_nb_ticket_carte(self):
        caisse = Caisse()
        carte = Carte(42,21,7)

        caisse.inserer_carte(carte)
        self.assertEqual(21, caisse.nb_ticket())

class TestPaiementAvecTicket(unittest.TestCase):
    def setUp(self):
        self.caisse = Caisse()
        self.carte = Carte(42,10,7)
        self.caisse.inserer_carte(self.carte)


    def test_paiement_repas_avec_solde_suffisant_avec_ticket(self):
        self.caisse.payer_repas_avec_ticket(9)
        self.assertEqual(9,self.carte.nb_ticket())
        self.assertEqual(40,self.carte.solde())

    def test_paiement_repas_moins_cher_que_ticket(self):
        self.caisse.payer_repas_avec_ticket(6)
        self.assertEqual(9,self.carte.nb_ticket())
        self.assertEqual(42,self.carte.solde())

    def test_paiement_repas_egale_au_ticket(self):
        self.caisse.payer_repas_avec_ticket(7)
        self.assertEqual(9,self.carte.nb_ticket())
        self.assertEqual(42,self.carte.solde())

    def test_payer_repas_sans_carte(self):
        caisse = Caisse()
        with self.assertRaises(CarteManquanteError):
            caisse.payer_repas_avec_ticket(9)

    def test_payer_sans_ticket_sur_carte(self):
        caisse = Caisse()
        carte = Carte(42,0,7)
        caisse.inserer_carte(carte)
        with self.assertRaises(NbTicketInsuffisantError):
            caisse.payer_repas_avec_ticket(50)

    def test_payer_repas_plus_cher_que_le_solde(self):
        with self.assertRaises(SoldeInsuffisantError):
            self.caisse.payer_repas_avec_ticket(50)


class TestPaiementSansTicket(unittest.TestCase):
    def setUp(self):
        self.caisse = Caisse()
        self.carte = Carte(42,7,7)
        self.caisse.inserer_carte(self.carte)


    def test_paiement_repas_avec_solde_suffisant(self):
        self.caisse.payer_repas_sans_ticket(9)
        self.assertEqual(33, self.carte.solde())

    def test_payer_repas_sans_carte(self):
        caisse = Caisse()
        with self.assertRaises(CarteManquanteError):
            caisse.payer_repas_sans_ticket(9)

    def test_payer_repas_plus_cher_que_le_solde(self):
        with self.assertRaises(SoldeInsuffisantError):
            self.caisse.payer_repas_sans_ticket(50)
