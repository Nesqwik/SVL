# SVL 16-17 - M. Nebut
# CTD property-based testing

class Caisse:

    # invariant : self.en_attente ==> self.ref_courante != None
    # invariant : (not self.en_attente) ==> self.ref_courante == None
    
    # post : not self.en_attente
    # post : self.ref_courante == None
    def __init__(self, base, affichage):
        self.en_attente = False
        self.base = base
        self.ref_courante = None
        self.affichage = affichage

    # signals (EnAttenteDePeseeError e) : not self.en_attente
    # post : self.en_attente
    # post : self.ref_courante == reference       
    def ajouter(self, reference):
        if self.en_attente_pesee():
            raise EnAttenteDePeseeError()
        produit = self.base.get(reference)
        self.affichage.afficher(produit)
        self.en_attente = True
        self.ref_courante = reference

    def en_attente_pesee(self):
        return self.en_attente

    # signals (ReferenceNonPasseeError e) : not self.en_attente
    # signals (ValueError e) : poid <= 0
    # signals (PeseeIncoherenteErreur e) : not self.base.est_autorise(self.ref_courante, poid)
    # post : not self.en_attente
    # post : self.ref_courante == None
    def notification_ajout_balance(self, poid):
        if not self.en_attente_pesee():
            raise ReferenceNonPasseeError()
        if poid <= 0:
            raise ValueError()
        if not self.base.est_autorise(self.ref_courante, poid):
             raise PeseeIncoherenteErreur()
        self.en_attente = False
        #self.ref_courante = None
        
class EnAttenteDePeseeError(Exception):
    pass

class ReferenceNonPasseeError(Exception):
    pass

class PeseeIncoherenteErreur(Exception):
    pass

class RefInconnueError(Exception):
    pass
