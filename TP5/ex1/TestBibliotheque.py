# SVL 1617 - M. Nebut
# CTD4 - exo bibliotheque

# test emprunter un livre
# - nominal : creation et stockage d'un emprunt
# - quota livre atteint : erreur
# - livre non empruntable : erreur
# - livre déjà emprunte : erreur
# - on peut peut le 20eme, pas le 21eme


from Bibliotheque import *

import unittest
from mockito import *


class TestEmprunterCreeUnEmprunt(unittest.TestCase):
    def test_emprunter_un_livre_cree_un_emprunt_avec_utilisateur_inconnu(self):
        fabrique_emprunt = mock()
        bibliotheque = Bibliotheque(fabrique_emprunt)

        utilisateur = mock()
        livre = mock()
        emprunt = mock()

        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(emprunt)

        nouvel_emprunt = bibliotheque.emprunter(utilisateur, livre)

        self.assertEqual(nouvel_emprunt, emprunt)

    def test_emprunter_un_livre_cree_un_emprunt_avec_utilisateur_connu(self):
        fabrique_emprunt = mock()
        bibliotheque = Bibliotheque(fabrique_emprunt)

        utilisateur = mock()
        bibliotheque.emprunts[utilisateur] = []
        livre = mock()
        emprunt = mock()

        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(emprunt)

        nouvel_emprunt = bibliotheque.emprunter(utilisateur, livre)

        self.assertEqual(nouvel_emprunt, emprunt)


# SUITE : TP5 Exercice 1 - Bibliotheque
# Test rendre un livre
# - nominal : Rentre un livre avant 30 jours renvoie ok
# - rendre après 30 jours : erreur
# - livre deja rendu : erreur
# - livre non emprunté : erreur

class TestRetourLivre(unittest.TestCase):
    def test_retour_livre_avant_30_jours(self):
        emprunt = mock()
        fabrique_emprunt = mock()
        utilisateur = mock()
        livre = mock()
        bibliotheque = Bibliotheque(fabrique_emprunt)

        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(emprunt)
        when(emprunt).get_utilisateur().thenReturn(utilisateur)
        when(emprunt).est_en_retard().thenReturn(False)

        bibliotheque.emprunter(utilisateur, livre)

        self.assertTrue(True, bibliotheque.rendre(emprunt))

    def test_retour_livre_apres_30_jours(self):

        emprunt = mock()
        fabrique_emprunt = mock()
        utilisateur = mock()
        livre = mock()
        bibliotheque = Bibliotheque(fabrique_emprunt)

        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(emprunt)
        when(emprunt).get_utilisateur().thenReturn(utilisateur)
        when(emprunt).est_en_retard().thenReturn(True)

        bibliotheque.emprunter(utilisateur, livre)

        with self.assertRaises(RetourEnRetardError):
            bibliotheque.rendre(emprunt)

    def test_retour_deja_effectue(self):
        fabrique_emprunt = mock()
        emprunt = mock()
        utilisateur = mock()
        livre = mock()

        bibliotheque = Bibliotheque(fabrique_emprunt)

        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(emprunt)
        when(emprunt).get_utilisateur().thenReturn(utilisateur)
        when(emprunt).est_en_retard().thenReturn(False)

        bibliotheque.emprunter(utilisateur, livre)

        self.assertTrue(True, bibliotheque.rendre(emprunt))
        with self.assertRaises(EmpruntNonExistantError):
            bibliotheque.rendre(emprunt)

    def test_emprunt_non_effectue(self):
        bibliotheque = Bibliotheque(None)

        with self.assertRaises(EmpruntNonExistantError):
            bibliotheque.rendre(mock())
