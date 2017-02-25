# SVL 1617 - M. Nebut
# CTD4 - exo bibliotheque

# test emprunter un livre
# - nominal : creation et stockage d'un emprunt
# - quota livre atteint : erreur
# - livre non empruntable : erreur
# - livre déjà emprunte : erreur
# - on peut peut le 20eme, pas le 21eme

from bibliotheque import *

import unittest
from mockito import *

class TestEmprunterCreeUnEmprunt(unittest.TestCase):

    def test_emprunter_un_livre_cree_un_emprunt(self):
        fabrique_emprunt = mock()
        service_emprunt = ServiceEmprunt(fabrique_emprunt)

        utilisateur = mock()
        livre = mock()
        emprunt = mock()

        when(fabrique_emprunt).creer_emprunt(utilisateur, livre).thenReturn(emprunt)

        nouvel_emprunt = service_emprunt.emprunter(utilisateur, livre)

        self.assertEqual(nouvel_emprunt, emprunt)

    def test_rendre_un_livre_non_retard(self):
        service_emprunt = ServiceEmprunt(mock())
        emprunt = mock()
        when(emprunt).est_en_retard().thenReturn(False)

        service_emprunt.rendre(emprunt)

        verify(emprunt,times=1).rendre()
        verify(emprunt,times=1).est_en_retard()

    def test_rendre_un_livre_en_retard(self):
        service_emprunt = ServiceEmprunt(mock())
        emprunt = mock()
        when(emprunt).est_en_retard().thenReturn(True)

        with self.assertRaises(RenduEnRetardException):
            service_emprunt.rendre(emprunt)

        verify(emprunt,times=1).rendre()
        verify(emprunt,times=1).est_en_retard()
