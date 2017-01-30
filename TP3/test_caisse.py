import unittest
from mockito import mock, when, verify

from caisse import *

class TestLaCarteEstInsereeEtRetireeDeLaCaisse(unittest.TestCase):
    def test_inserer_retirer_carte(self):
        caisse = Caisse()
        carte = mock()

        caisse.inserer_carte(carte)

        self.assertEqual(carte, caisse.retirer_carte())

    def test_retirer_carte_sans_inserer(self):
        caisse = Caisse()

        with self.assertRaises(CarteManquanteError):
            caisse.retirer_carte()



class TestLaCaisseVisualiseLesSoldesDeLaCarte(unittest.TestCase):

    def test_visualiser_solde_carte(self):
        caisse = Caisse()
        carte = mock()

        when(carte).solde().thenReturn(42)

        caisse.inserer_carte(carte)
        self.assertEqual(42, caisse.solde())

    def test_visualiser_nb_ticket_carte(self):
        caisse = Caisse()
        carte = mock()

        when(carte).nb_ticket().thenReturn(21)

        caisse.inserer_carte(carte)
        self.assertEqual(21, caisse.nb_ticket())

class TestPaiementAvecTicket(unittest.TestCase):
    def setUp(self):
        self.caisse = Caisse()
        self.carte = mock()

        when(self.carte).solde().thenReturn(42)
        when(self.carte).nb_ticket().thenReturn(10)
        when(self.carte).prix_ticket().thenReturn(7)

        self.caisse.inserer_carte(self.carte)


    def test_paiement_repas_avec_solde_suffisant_avec_ticket(self):
        self.caisse.payer_repas_avec_ticket(9)

        verify(self.carte).utiliser_ticket()
        verify(self.carte, times=1).debiter(2)

    def test_paiement_repas_moins_cher_que_ticket(self):
        self.caisse.payer_repas_avec_ticket(6)
        verify(self.carte).utiliser_ticket()
        verify(self.carte, times=0).debiter()

    def test_paiement_repas_egale_au_ticket(self):
        self.caisse.payer_repas_avec_ticket(7)
        verify(self.carte).utiliser_ticket()
        verify(self.carte, times=0).debiter()

    def test_payer_repas_sans_carte(self):
        caisse = Caisse()
        with self.assertRaises(CarteManquanteError):
            caisse.payer_repas_avec_ticket(9)

    def test_payer_sans_ticket_sur_carte(self):
        when(self.carte).nb_ticket().thenReturn(0)
        with self.assertRaises(NbTicketInsuffisantError):
            self.caisse.payer_repas_avec_ticket(50)

    def test_payer_repas_plus_cher_que_le_solde(self):
        with self.assertRaises(SoldeInsuffisantError):
            self.caisse.payer_repas_avec_ticket(50)


class TestPaiementSansTicket(unittest.TestCase):
    def setUp(self):
        self.caisse = Caisse()
        self.carte = mock()

        when(self.carte).solde().thenReturn(42)
        self.caisse.inserer_carte(self.carte)


    def test_paiement_repas_avec_solde_suffisant(self):
        self.caisse.payer_repas_sans_ticket(9)
        verify(self.carte, times=1).debiter(9)

    def test_payer_repas_sans_carte(self):
        caisse = Caisse()
        with self.assertRaises(CarteManquanteError):
            caisse.payer_repas_sans_ticket(9)

    def test_payer_repas_plus_cher_que_le_solde(self):
        with self.assertRaises(SoldeInsuffisantError):
            self.caisse.payer_repas_sans_ticket(50)
