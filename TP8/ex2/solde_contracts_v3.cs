using System;
using System.Diagnostics.Contracts;

public class Compte {
	public double solde;
	public int decouvert;

    [ContractInvariantMethod]
    void ObjectInvariant () {
        Contract.Invariant(solde >= -decouvert);
        Contract.Invariant(decouvert >= 0);
    }

    public Compte() {
        Contract.Ensures(solde == 0.0);
        Contract.Ensures(decouvert == 0);
        decouvert = 0;
        solde = 0.0;
    }


    public void autoriserDecouvert(int maxDecouvert) {
        Contract.Requires(maxDecouvert >= 0);
        Contract.Requires(-maxDecouvert < solde);
        Contract.Ensures(maxDecouvert == decouvert);
        decouvert = maxDecouvert;
    }

	public void credit(double valeur) {
        Contract.Requires(valeur >= 0);
        Contract.Ensures(solde == Contract.OldValue(solde) + valeur);
        solde += valeur;
	}

	public void debit(double valeur) {
	    Contract.Requires(valeur >= 0);
        Contract.Requires(valeur <= solde + decouvert);
        Contract.Ensures(solde >= -decouvert);
        solde -= valeur;
    }
}

