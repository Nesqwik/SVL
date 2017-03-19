/*
SVL 16-17 M. Nebut
ex de spéc JML - CTD7 prog par contrats.
*/


package restaurant_entreprise;

public class Caisse {

    private /*@ nullable @*/ /*@ spec_public @*/ Carte la_carte;
    // private Carte la_carte;

    public Caisse() {
	this.la_carte = null;
    }
    
    // public Carte carte() {
    // 	return this.la_carte;
    // }

    //@ ensures this.la_carte == carte;
    public void insererCarte(Carte carte) {
	this.la_carte = carte;
    }

    //@ ensures \result == la_carte.le_solde;
    //@ signals (CarteManquanteException e) this.la_carte == null;
    public double solde() throws CarteManquanteException {
	if (this.la_carte == null) {
	    throw new CarteManquanteException();
	}
	return this.la_carte.solde();
    }

    //@ ensures la_carte.le_solde == \old(la_carte.le_solde) - montant_repas;
    //@ signals (CarteManquanteException e) this.la_carte == null;
    //@ signals (IllegalArgumentException e) montant_repas < 0;
    //@ signals (DebitException e) montant_repas > la_carte.le_solde;
    public void payer_repas_sans_ticket(double montant_repas) throws IllegalArgumentException, DebitException, CarteManquanteException {
	if (this.la_carte == null)
	    throw new CarteManquanteException();
	if (montant_repas < 0) 
	    throw new IllegalArgumentException();
	if (montant_repas > this.solde())
	    throw new DebitException();	    
	
	this.la_carte.debiter(montant_repas);
    }

    //@ ensures this.la_carte.le_nb_tickets == 0 ==> la_carte.le_solde == \old(la_carte.le_solde) - montant_repas;
    /*@ ensures (this.la_carte.le_nb_tickets > 0 && this.la_carte.le_prix_d_un_ticket >= montant_repas) ==>
          (this.la_carte.le_nb_tickets == \old(this.la_carte.le_nb_tickets) - 1
                         && this.la_carte.le_solde == \old(this.la_carte.le_solde));
     @*/
    /*@ ensures (this.la_carte.le_nb_tickets > 0 && this.la_carte.le_prix_d_un_ticket < montant_repas) ==>
          (this.la_carte.le_nb_tickets == \old(this.la_carte.le_nb_tickets) - 1
              && this.la_carte.le_solde == \old(this.la_carte.le_solde) - 
                                (montant_repas - this.la_carte.le_prix_d_un_ticket));
     @*/
    //@ signals (CarteManquanteException e) this.la_carte == null;
    //@ signals (IllegalArgumentException e) montant_repas < 0;
    //@ signals (DebitException e) this.la_carte.le_nb_tickets == 0 && this.la_carte.le_solde < montant_repas;
    public void payer_repas_avec_ticket(double montant_repas) throws IllegalArgumentException, DebitException, CarteManquanteException {
	if (this.la_carte == null)
	    throw new CarteManquanteException();
	if (montant_repas < 0) 
	    throw new IllegalArgumentException();
	if (this.la_carte.nb_tickets() == 0)
	    if (this.la_carte.solde() >= montant_repas)
		this.la_carte.debiter(montant_repas);
	    else
		throw new DebitException();
	else {
	    if (this.la_carte.prix_ticket() < montant_repas)
		this.la_carte.debiter(montant_repas - this.la_carte.prix_ticket());
	    this.la_carte.consommer_ticket();
	}
    }
    
     public static void main(String args[]) throws Exception {
	 Caisse machine = new Caisse();
	 Carte carte = new Carte(9.0, 10, 20.0);
	 //machine.solde();
	 //machine.payer_repas_sans_ticket(5.0);
	 machine.insererCarte(carte);
	 machine.solde();
	 machine.payer_repas_avec_ticket(8.0);
	 machine.payer_repas_avec_ticket(18.0);
	 Carte carte_sans_tickets = new Carte(9.0, 0, 20.0);
	 machine.insererCarte(carte_sans_tickets);
	 machine.payer_repas_avec_ticket(18.0);
	 //machine.payer_repas_avec_ticket(118.0);
	 
	 System.out.println("fin");
     }
    
}
