# SVL 1617 - M. Nebut
# CTD4 - exo service et sessions


from service import *

import unittest
from mockito import *

# tests prevus :
# test de l'objet initial : aucune session courante
# test de l'ajout de session
# - ajouter une session
# - ajouter 3 sessions
# test du kill :
# - sans sessions courantes : oracle ?
# - tuer avec 3 sessions tue les 3 sessions

class TestAjouterDesSessions(unittest.TestCase):

    def test_ajouter_une_session_courante(self):
        session_number_policy = mock()
        sessions = Sessions(session_number_policy)
        session = mock()
        sessions.add(session)
        self.assertIn(session, sessions.current_sessions())

    def test_ajouter_trois_sessions_courantes(self):
        session_number_policy = mock()
        sessions = Sessions(session_number_policy)
        
        session1 = mock()
        session2 = mock()
        session3 = mock()
        sessions.add(session1)
        sessions.add(session2)
        sessions.add(session3)
        self.assertIn(session1, sessions.current_sessions())
        self.assertIn(session2, sessions.current_sessions())
        self.assertIn(session3, sessions.current_sessions())

class TestTuerLesSessionsCourantes(unittest.TestCase):

    # tangent
    def test_tuer_quand_pas_de_sessions_courantes_pas_d_erreur(self):
        session_number_policy = mock()
        sessions = Sessions(session_number_policy)
        sessions.kill()
        self.assertEqual([], sessions.current_sessions())

    def test_tuer_le_gestionnaire_tue_ses_sessions(self):
        session_number_policy = mock()
        sessions = Sessions(session_number_policy)
        
        session1 = mock()
        session2 = mock()
        session3 = mock()
        sessions.add(session1)
        sessions.add(session2)
        sessions.add(session3)

        sessions.kill()
        
        verify(session1).kill()
        verify(session2).kill()
        verify(session3).kill()


class TestNombreSessionsCourantesLimiteA1(unittest.TestCase):

    # tester que ajout 1 session ne leve pas l'exception
    # TODO
    
# NB : si on avait mocke can_add() au lieu de capacity_reached
# il aurait ete necessaire de stubber par des when
# la reponse a can_add dans tous les tests precedents.
# ici on s'en sort par la reponse None par defaut de mockito
# et None interprete comme False ds une expr bool.
# c'est aussi bien de mettre les when explicites.

    def test_ajouter_une_seconde_session_produit_une_erreur(self):
        session_number_policy = mock()

        sessions = Sessions(session_number_policy)

        session1 = mock()
        session2 = mock()

        when(session_number_policy).capacity_reached(0).thenReturn(False)
        sessions.add(session1)
        when(session_number_policy).capacity_reached(1).thenReturn(True)
        with self.assertRaises(LimiteNombreSessionAtteintError):
            sessions.add(session2)

        

    
