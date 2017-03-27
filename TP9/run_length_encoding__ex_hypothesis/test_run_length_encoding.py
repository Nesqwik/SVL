# SVL 16-17 - M. Nebut
# CTD property-based testing
# ex d'utilisation d'Hypothesing, le code est tiré de
# https://hypothesis.readthedocs.io/en/master/quickstart.html

# peut se lancer avec
# nosetests test_run_length_encoding.py
# ou pour voir les stats avec 
# pytest --hypothesis-show-statistics test_run_length_encoding.py

from run_length_encoding import *

from nose.tools import assert_equal

from hypothesis import given, example
from hypothesis.strategies import text

from hypothesis import settings, Verbosity

@settings(verbosity=Verbosity.verbose) # affichage des s choisis en cas d'échec
@given(s=text())
@example('')
def test_decode_inverts_encode(s):
    assert_equal(decode(encode(s)), s)
