import unittest

import carte
from carte import *

class TestCreationCarteAvecSoldeEtTicket(unittest.TestCase):
    def test_creer_carte_avec_solde_et_ticket(self):
        c = Carte(42, 42, 7)
        self.assertEqual(42, c.nb_ticket())
        self.assertEqual(42, c.solde())
        self.assertEqual(7, c.prix_ticket())
