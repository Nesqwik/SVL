import unittest
from mockito import mock, when, verify

from Filtre import *

class TestFiltreParPriorite(unittest.TestCase):
    def test_filtre_priorite_inf_5_sur_log_4(self):
        filtre = Filtre()
        log = mock()
        when(log).get_priority().thenReturn(4)
        self.assertEqual(None, filtre.filtrer_par_priorite_inf(5, log))

    def test_filtre_priorite_inf_5_sur_log_5(self):
        filtre = Filtre()
        log = mock()
        when(log).get_priority().thenReturn(5)
        self.assertEqual(log, filtre.filtrer_par_priorite_inf(5, log))

    def test_filtre_priorite_inf_5_sur_log_6(self):
        filtre = Filtre()
        log = mock()
        when(log).get_priority().thenReturn(6)
        self.assertEqual(log, filtre.filtrer_par_priorite_inf(5, log))
