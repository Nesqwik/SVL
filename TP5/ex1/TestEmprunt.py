# Test de la classe emprunt :
# - Test nominal : création emprunt avec utilisateur et livre : retourne un emprunt contenant utilisateur et livre et date du jour pour date de l'emprunt
#    - get_utilisateur est égale à l'utilisateur passé en paramètre
#    - get_livre est égale à l'utilisateur passé en paramètre
#    - get_date_emprunt est égale à la date du jour
#
# - Test est_en_retard :
#   - si la date du rendu - la date de l'emprunt est <= à une durée défini (30 jours) : renvoie vrai
#   - si la date du rendu - la date de l'emprunt est < à une durée défini (30 jours) : renvoie faux


from Emprunt import *

import unittest
import datetime
from mockito import *

class TestCreeUnEmprunt(unittest.TestCase):

    def test_creer_emprunt_avec_utilisateur_et_livre(self):
        utilisateur = mock()
        livre = mock()
        emprunt = Emprunt(utilisateur, livre)

        self.assertIsNotNone(emprunt)
        self.assertEqual(utilisateur, emprunt.get_utilisateur())
        self.assertEqual(livre, emprunt.get_livre())
        self.assertEqual(datetime.date.today(), emprunt.get_date_emprunt())

    def test_retour_en_retard_plus_de_30_jours(self):
        utilisateur = mock()
        livre = mock()

        # création de la date d'emprunt
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 1)
        datetime.date = NewDate

        emprunt = Emprunt(utilisateur, livre)
        # création de la date de retour
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 2, 1)
        datetime.date = NewDate
        self.assertTrue(emprunt.est_en_retard())

    def test_retour_ok_moins_de_30_jours(self):
        utilisateur = mock()
        livre = mock()

        # création de la date d'emprunt
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 1)
        datetime.date = NewDate

        emprunt = Emprunt(utilisateur, livre)
        # création de la date de retour
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 30)
        datetime.date = NewDate
        self.assertFalse(emprunt.est_en_retard())

    def test_retour_ok_exactement_30_jours(self):
        utilisateur = mock()
        livre = mock()

        # création de la date d'emprunt
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 1)
        datetime.date = NewDate

        emprunt = Emprunt(utilisateur, livre)
        # création de la date de retour
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 31)
        datetime.date = NewDate
        self.assertFalse(emprunt.est_en_retard())
