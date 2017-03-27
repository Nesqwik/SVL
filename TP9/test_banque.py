from nose.tools import assert_equal, assert_true

from hypothesis import given, example
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule
from hypothesis import strategies as st

from hypothesis import settings, Verbosity

import mockito
from mockito import mock, when, verify

from banque import *

@settings(verbosity=Verbosity.verbose) # affichage des s choisis en cas d'échec
@given(debit=st.integers(min_value=1, max_value=9999))
def test_debiter_bornes_valides(debit):
    c = Compte()
    c.crediter(10000)
    c.debiter(debit)
    assert_true(c.montant >= 0)
    assert_true(c.montant <= 10000)


@settings(verbosity=Verbosity.verbose) # affichage des s choisis en cas d'échec
@given(credit=st.integers(min_value=1))
def test_crediter(credit):
    c = Compte()
    c.crediter(credit)
    assert_equal(c.montant,credit)

@settings(verbosity=Verbosity.verbose) # affichage des s choisis en cas d'échec
@given(decouvert1=st.integers(max_value=-1, min_value=-10000), decouvert2=st.integers(max_value=-1, min_value=-5000), credit=st.integers(min_value=1, max_value=10000), debit=st.integers(min_value=1, max_value=10000))
def test_autoriser_decouvert(decouvert1,decouvert2, debit, credit):
    c = Compte()
    c.crediter(credit)
    c.autoriser_decouvert(decouvert1)
    try:
        c.debiter(debit)
        c.autoriser_decouvert(decouvert2)
        assert_true(c.montant >= decouvert2)
    except ValueError:
        pass
