/*
SVL 16-17 M. Nebut
ex de spéc JML - CTD7 prog par contrats.
 */
package restaurant_entreprise;

public class Carte {

    private /*@ spec_public @*/ double le_solde;
    private /*@ spec_public @*/ int le_nb_tickets;
    private /*@ spec_public @*/ double le_prix_d_un_ticket;

    //@ public invariant this.le_solde >= 0;
    //@ public invariant this.le_nb_tickets >= 0;
    //@ public invariant this.le_prix_d_un_ticket >= 0;

    //@ requires prix_ticket > 0;
    //@ ensures this.le_solde == 0.0;
    //@ ensures this.le_nb_tickets == 0;
    //@ ensures this.le_prix_d_un_ticket == prix_ticket;
    public Carte(double prix_ticket) {
	this.le_solde = 0.0;
	this.le_nb_tickets = 0;
	this.le_prix_d_un_ticket = prix_ticket;
    }

    //@ requires prix_ticket > 0;
    //@ requires solde > 0;
    //@ requires nb_tickets >= 0;
    //@ ensures this.le_prix_d_un_ticket == prix_ticket;
    //@ ensures this.le_solde == solde;
    //@ ensures this.le_nb_tickets == nb_tickets;
    public Carte(double prix_ticket, int nb_tickets, double solde) {
	this.le_solde = solde;
	this.le_nb_tickets = nb_tickets;
	this.le_prix_d_un_ticket = prix_ticket;
    }

    //@ ensures \result == this.le_prix_d_un_ticket;
    public double prix_ticket() {
	return this.le_prix_d_un_ticket;
    }

    //@ ensures \result == this.le_solde;
    public double solde() {
	return this.le_solde;
    }

    //@ ensures \result == this.le_nb_tickets;
    public int nb_tickets() {
	return this.le_nb_tickets;
    }

    
    //@ signals (DebitException e) a_debiter > this.solde();
    //@ signals (IllegalArgumentException e) a_debiter < 0;
    //@ ensures this.solde() == \old(this.solde() - a_debiter);
    public void debiter(double a_debiter) throws IllegalArgumentException, DebitException {
	if (a_debiter < 0) 
	    throw new IllegalArgumentException();
	if (this.solde() < a_debiter) 
	    throw new DebitException();
	this.le_solde -= a_debiter;
    }

    //@ requires this.nb_tickets() > 0;
    //@ ensures this.nb_tickets() == \old(this.nb_tickets()) - 1;
    public void consommer_ticket() {	
	this.le_nb_tickets -= 1;
    }

    
    public static void main(String args[]) throws Exception {

	Carte carte_vide = new Carte(9);
	Carte carte_non_vide = new Carte(9, 10, 20.0);
	//Carte carte_non_vide2 = new Carte(0, 20.0);
	carte_non_vide.debiter(5.0);
	//carte_non_vide.debiter(100.0);
	carte_non_vide.consommer_ticket();
	System.out.println("fin");
    }
}
