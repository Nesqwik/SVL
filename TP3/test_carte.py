import carte
from carte import Carte

import unittest

class TestCredit(unittest.Case):
    def test_credit(selft):
        c = Carte()
        c.credit(10)
        self.assertEqual(10,c.get_balance())

    def test_credit_multiple(self):
        c = Carte()
        c.credit(21)
        c.credit(21)
        self.assertEqual(42,c.get_balance())
    
    def test_credit_negatif(self):
        c = Carte()
        with self.assertRaise(ValueError):
            c.credit(-10)

    def test_credit_zero(self):
        c=Carte()
        with self.assertRaise(ValueError):
            c.credit(0)
