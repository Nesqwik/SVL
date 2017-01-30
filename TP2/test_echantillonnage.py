import unittest
import echantillonnage
from echantillonnage import Echantillonnage

class TestEchantillonnage(unittest.TestCase):

    def test_sous_echantillonnage_simple(self):
        e = Echantillonnage()
        self.assertEqual([1,2,3], e.sous_echantillonnage([1,2,3],3,4))

    def test_sous_echantillonnage_taille_variable_no_frequence(self):
        e = Echantillonnage()
        self.assertEqual([1,2,3], e.sous_echantillonnage([1,2,3,4,5,6],3,7))

    def test_sous_echantillonnage_taille_superieur_array(self):
        e = Echantillonnage()
        self.assertEqual([1,2,3,4,5], e.sous_echantillonnage([1,2,3,4,5],10,11))

    def test_sous_echantillonnage_frequence_deux_fois_entiere(self):
        e = Echantillonnage()
        self.assertEqual([1,2,4,5], e.sous_echantillonnage([1,2,3,4,5],2,3))

    def test_sous_echantillonnage_frequence_quatre_fois_derniere_non_entiere(self):
        e = Echantillonnage()
        self.assertEqual([1,2,4,5,7,8,10], e.sous_echantillonnage([1,2,3,4,5,6,7,8,9,10],2,3))

    def test_sous_echantillonnage_frequence_inferieur_taille(self):
        e = Echantillonnage()
        self.assertEqual([1,2,3,4,3,4,5,6,5,6,7,8,7,8,9,9], e.sous_echantillonnage([1,2,3,4,5,6,7,8,9],4,2))
