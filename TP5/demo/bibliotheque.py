# SVL 1617 - M. Nebut
# CTD4 - exo bibliotheque

class ServiceEmprunt:

    def __init__(self, fabrique_emprunt):
        self.fabrique_emprunt = fabrique_emprunt

    def emprunter(self, utilisateur, livre):
        # surtout pas
        #return Emprunt(livre, utilisateur)
        return self.fabrique_emprunt.creer_emprunt(utilisateur, livre)

    def rendre(self, emprunt):
        emprunt.rendre()
        if emprunt.est_en_retard():
            raise RenduEnRetardException

class RenduEnRetardException(Exception):
    pass
