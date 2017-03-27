# SVL 16-17 - M. Nebut
# CTD property-based testing

from caisse_automatique import *

from mockito import *

from hypothesis import strategies as st
from hypothesis import assume, settings
from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule

import unittest

class CaisseMachine(RuleBasedStateMachine):

    liste_caisses = Bundle('Caisses')

    @rule(target=liste_caisses)
    def nouvelle_caisse(self):
        base = mock()
        when(base).est_autorise(any(), any()).thenReturn(True)
        return Caisse(base, mock())

    @rule(caisse=liste_caisses)
    def ajouter_produit_machine(self, caisse):
        try:
            caisse.ajouter(mock())
        except EnAttenteDePeseeError:
            pass #vaudrait mieux signaler à hypothesis pour les stats
        
    @rule(caisse=liste_caisses, poid=st.integers(min_value=0).filter(lambda s : s != 0))
    def notifier_ajout_balance_machine(self, caisse, poid):
        try:
            caisse.notification_ajout_balance(poid)
        except ReferenceNonPasseeError:
            pass
        
#    @settings(max_examples=100000)
    @rule(caisse=liste_caisses)
    def test_reference_correcte(self, caisse):
        if caisse.en_attente :
            assert caisse.ref_courante is not None
        else:
            assert caisse.ref_courante is None
        
TestCaisseMachine = CaisseMachine.TestCase

if __name__ == '__main__':
    unittest.main()
