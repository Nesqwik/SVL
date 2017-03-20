using System;
using System.Diagnostics.Contracts;

public class Compte {
	public int solde;
	public int decouvert;

    [ContractInvariantMethod]
    void ObjectInvariant () {
        Contract.Invariant(solde >= 0);
    }

    public Compte() {
        Contract.Ensures(solde == 0);
        solde = 0;
    }

	public void credit(int valeur) {
        Contract.Requires(valeur >= 0);
        Contract.Ensures(solde == Contract.OldValue(solde) + valeur);
        solde += valeur;
	}

	public void debit(int valeur) {
	    Contract.Requires(valeur >= 0);
        Contract.Requires(valeur <= solde);
        Contract.Ensures(solde >= 0);
        solde -= valeur;
    }
}

