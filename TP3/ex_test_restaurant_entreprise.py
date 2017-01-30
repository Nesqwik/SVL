# demo SVL - CTD3 - 1617 - M. Nebut
# test des interactions avec mockito

import unittest
from mockito import mock, when, verify

from restaurant_entreprise import *

# test de la Caisse

# fonctionnalite : consulter le solde de la carte
# - le solde est celui de la carte
# - carte pas inseree : echec

class TestLaCaisseVisualiseLeSoldeDeLaCarte(unittest.TestCase):

    def test_le_solde_est_celui_de_la_carte(self):
        # setup
        caisse = Caisse()
        carte = mock()

        # expectations
        when(carte).solde().thenReturn(10)

        # exercice
        caisse.inserer(carte)
        montant = caisse.solde()

        # verify
        self.assertEqual(montant, 10)

    def test_carte_pas_inseree_la_consultation_echoue(self):
        caisse = Caisse()

        self.assertRaises(CarteManquanteError,
                          caisse.solde)

# fonctionnalite : payer un repas sans ticket
# - la caisse debite la carte
# - le paiement echoue car carte insuffisamment approvisionnee

class TestLucPayeUnRepasSansTicket(unittest.TestCase):

    def test_la_caisse_debite_la_carte(self):
        caisse = Caisse()
        carte = mock()
        caisse.inserer(carte)

        caisse.payer_repas_sans_ticket(7)

        verify(carte).debiter(7)
        # pas de test d'état sur mock, donc pas de vérification par un assertEqual sur le solde de la carte

    def test_pas_suffisamment_d_argent_le_paiement_echoue(self):
        caisse = Caisse()
        carte = mock()
        
        caisse.inserer(carte)
        when(carte).debiter(7).thenRaise(SoldeInsuffisantError())

        self.assertRaises(SoldeInsuffisantError, caisse.payer_repas_sans_ticket, 7)
