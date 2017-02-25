# SVL 1617 - M. Nebut
# CTD4 - exo bibliotheque

# Suite TP5 - Exercice 1 bibliotheque

class Bibliotheque:

    def __init__(self, fabrique_emprunt):
        self.fabrique_emprunt = fabrique_emprunt
        self.emprunts = {}

    def emprunter(self, utilisateur, livre):
        emprunt = self.fabrique_emprunt.creer_emprunt(utilisateur, livre)
        if not utilisateur in self.emprunts:
            self.emprunts[utilisateur] = []

        self.emprunts[utilisateur].append(emprunt)
        return emprunt

    def rendre(self, emprunt):
        if not emprunt.get_utilisateur() in self.emprunts:
            raise EmpruntNonExistantError

        if not emprunt in self.emprunts[emprunt.get_utilisateur()]:
            raise EmpruntNonExistantError

        self.emprunts[emprunt.get_utilisateur()].remove(emprunt)

        if emprunt.est_en_retard():
            raise RetourEnRetardError()
        else:
            return True


class RetourEnRetardError(Exception):
    pass

class EmpruntNonExistantError(Exception):
    pass
