import unittest
import mockito
from mockito import mock, when, verify
from UserCreator import *

class TestCreationUtilisateurNomPrenomLogin (unittest.TestCase):
    def test_creer_utilisateur(self):
        user_factory = mock()
        user_creator = UserCreator(user_factory)
        user = mock()
        when(user_factory).createUser("nom","prenom","login").thenReturn(user)
        self.assertTrue(user_creator.createUser("nom","prenom","login"))

    def test_creer_utilisateur_et_stockage(self):
        user_factory = mock()
        user_creator = UserCreator(user_factory)
        user = mock()
        when(user_factory).createUser("nom","prenom","login").thenReturn(user)
        user_creator.createUser("nom","prenom","login")
        self.assertEqual(user, user_creator.getUser("login"))

    def test_creer_plusieurs_utilisateurs_et_stockage(self):
        user_factory = mock()
        user_creator = UserCreator(user_factory)
        user1 = mock()
        user2 = mock()
        user3 = mock()
        when(user_factory).createUser("nom1","prenom1","login1").thenReturn(user1)
        when(user_factory).createUser("nom2","prenom2","login2").thenReturn(user2)
        when(user_factory).createUser("nom3","prenom3","login3").thenReturn(user3)
        user_creator.createUser("nom1","prenom1","login1")
        user_creator.createUser("nom2","prenom2","login2")
        user_creator.createUser("nom3","prenom3","login3")
        self.assertEqual(user1, user_creator.getUser("login1"))
        self.assertEqual(user2, user_creator.getUser("login2"))
        self.assertEqual(user3, user_creator.getUser("login3"))

    def test_creer_utilisateur_login_existant_erreur(self):
        user_factory = mock()
        user_creator = UserCreator(user_factory)
        user1 = mock()
        user2 = mock()
        when(user_factory).createUser("nom1","prenom1","login").thenReturn(user1)
        when(user_factory).createUser("nom2","prenom2","login").thenReturn(user2)
        user_creator.createUser("nom1","prenom1","login")
        with self.assertRaises(LoginAlreadyExistError):
            user_creator.createUser("nom2","prenom2","login")

class TestCreationUtilisateurNomPrenomLoginGenere (unittest.TestCase):

    def test_generer_login_plan_A_format_valide_nom_taille_sup_8_char(self):
        user_creator = UserCreator(mock())
        self.assertEqual("NomDePlu",user_creator.generateLoginMethodA("NomDePlusDe8Char"))

    def test_generer_login_plan_A_format_valide_nom_taille_9_char(self):
        user_creator = UserCreator(mock())
        self.assertEqual("NomDe9Ch",user_creator.generateLoginMethodA("NomDe9Cha"))

    def test_generer_login_plan_A_format_valide_nom_taille_8_char(self):
        user_creator = UserCreator(mock())
        self.assertEqual("Nom8Char",user_creator.generateLoginMethodA("Nom8Char"))

    def test_generer_login_plan_A_format_valide_nom_taille_moins_8_char(self):
        user_creator = UserCreator(mock())
        self.assertEqual("Nom",user_creator.generateLoginMethodA("Nom"))

    def test_generer_login_plan_B_format_valide_nom_taille_sup_7_char(self):
        user_creator = UserCreator(mock())
        self.assertEqual("NomDePlP",user_creator.generateLoginMethodB("NomDePlusDe7Char", "Prenom"))

    def test_generer_login_plan_B_format_valide_nom_taille_8_char(self):
        user_creator = UserCreator(mock())
        self.assertEqual("NomDe8CP",user_creator.generateLoginMethodB("NomDe8Ch", "Prenom"))

    def test_generer_login_plan_B_format_valide_nom_taille_7_char(self):
        user_creator = UserCreator(mock())
        self.assertEqual("Nom7ChaP",user_creator.generateLoginMethodB("Nom7Cha", "Prenom"))

    def test_generer_login_plan_B_format_valide_nom_taille_moins_7_char(self):
        user_creator = UserCreator(mock())
        self.assertEqual("NomP",user_creator.generateLoginMethodB("Nom","Prenom"))

    def test_creer_utilisateur_valide_login_genere_methode_A(self):
        user_factory = mock()
        user_creator = UserCreator(user_factory)
        user = mock()
        when(user_factory).createUser("nom","prenom","nom").thenReturn(user)
        self.assertTrue(user_creator.createUserNoCare("nom", "prenom"))
        self.assertEqual(user, user_creator.getUser("nom"))
