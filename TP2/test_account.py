import account
from account import Compte
import unittest

class TestCredit(unittest.TestCase):
    def test_credit(self):
        c = Compte()
        c.credit(10)
        self.assertEqual(10, c.get_balance())

    def test_credit_multiple(self):
        c = Compte()
        c.credit(10)
        c.credit(32)
        self.assertEqual(42, c.get_balance())

    def test_credit_negatif(self):
        c = Compte()
        with self.assertRaises(ValueError):
            c.credit(-10)

    def test_credit_zero(self):
        c = Compte()
        with self.assertRaises(ValueError):
            c.credit(0)


class TestDebit(unittest.TestCase):

    def test_debit(self):
        c = Compte()
        c.credit(10)
        c.debit(6)
        self.assertEqual(4, c.get_balance())

    def test_debit_multiple(self):
        c = Compte()
        c.credit(10)
        c.debit(5)
        c.debit(5)
        self.assertEqual(0, c.get_balance())

    def test_debit_decouvert(self):
        c = Compte()
        c.credit(5)
        with self.assertRaises(ValueError):
            c.debit(10)

    def test_debit_negatif(self):
        c = Compte()
        c.credit(10)
        with self.assertRaises(ValueError):
            c.debit(-5)

    def test_debit_zero(self):
        c = Compte()
        with self.assertRaises(ValueError):
            c.debit(0)
