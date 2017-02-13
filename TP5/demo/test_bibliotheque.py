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
