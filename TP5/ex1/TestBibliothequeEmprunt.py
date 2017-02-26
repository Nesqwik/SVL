# tests d'intégration de la classe "Emprunt" à la classe de gestion des emprunts "Bibliotheque"

# - cas nominal : emprunt puis retour dans les temps
# - cas nominal : emprunt puis retour dans les temps date limite
# - emprunt puis retour en retard : erreur retard
# - emprunt puis 2 retours : erreur emprunt inexistant
# - retour sans emprunt : erreur emprunt inexistant
#

from Emprunt import *
from Bibliotheque import *

import unittest
import datetime
from mockito import *

class TestBibliothequeEmprunt(unittest.TestCase):

    def test_nominal_emprunt_retour_dans_les_temps(self):
        # création de la date d'emprunt
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 1)
        datetime.date = NewDate

        utilisateur = mock()
        livre = mock()

        fabrique_emprunt = mock()
        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(Emprunt(utilisateur, livre))
        bibliotheque = Bibliotheque(fabrique_emprunt)
        emprunt = bibliotheque.emprunter(utilisateur, livre)

        # création de la date de retour
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 29)
        datetime.date = NewDate

        self.assertTrue(bibliotheque.rendre(emprunt))

    def test_nominal_emprunt_retour_dans_les_temps_date_limite(self):
        # création de la date d'emprunt
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 1)
        datetime.date = NewDate

        utilisateur = mock()
        livre = mock()

        fabrique_emprunt = mock()
        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(Emprunt(utilisateur, livre))
        bibliotheque = Bibliotheque(fabrique_emprunt)
        emprunt = bibliotheque.emprunter(utilisateur, livre)

        # création de la date de retour
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 31)
        datetime.date = NewDate

        self.assertTrue(bibliotheque.rendre(emprunt))


    def test_retour_en_retard_erreur(self):
        # création de la date d'emprunt
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 1)
        datetime.date = NewDate

        utilisateur = mock()
        livre = mock()

        fabrique_emprunt = mock()
        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(Emprunt(utilisateur, livre))
        bibliotheque = Bibliotheque(fabrique_emprunt)
        emprunt = bibliotheque.emprunter(utilisateur, livre)

        # création de la date de retour
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 2, 1)
        datetime.date = NewDate

        with self.assertRaises(RetourEnRetardError):
            bibliotheque.rendre(emprunt)


    def test_deux_retours_pour_un_emprunt_erreur(self):
        # création de la date d'emprunt
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 1)
        datetime.date = NewDate

        utilisateur = mock()
        livre = mock()

        fabrique_emprunt = mock()
        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(Emprunt(utilisateur, livre))
        bibliotheque = Bibliotheque(fabrique_emprunt)
        emprunt = bibliotheque.emprunter(utilisateur, livre)

        # création de la date de retour
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 29)
        datetime.date = NewDate

        bibliotheque.rendre(emprunt)
        with self.assertRaises(EmpruntNonExistantError):
            bibliotheque.rendre(emprunt)

    def test_retour_sans_emprunt_erreur(self):
        # création de la date d'emprunt
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 1)
        datetime.date = NewDate

        utilisateur = mock()
        livre = mock()

        fabrique_emprunt = mock()
        emprunt = Emprunt(utilisateur, livre)
        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(emprunt)
        bibliotheque = Bibliotheque(fabrique_emprunt)

        # création de la date de retour
        class NewDate(datetime.date):
            @classmethod
            def today(self):
                return self(2017, 1, 29)
        datetime.date = NewDate

        with self.assertRaises(EmpruntNonExistantError):
            bibliotheque.rendre(emprunt)
