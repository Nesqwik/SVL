using System;
using System.Diagnostics.Contracts;

public class Compte {
	public double solde;
	public int decouvert;

    invariant solde >= -decouvert;
    invariant decouvert >= 0 ;

    public Compte()
        ensures solde == 0.0;
        ensures decouvert == 0;
    {
        decouvert = 0;
        solde = 0.0;
    }


    public void autoriserDecouvert(int maxDecouvert)
        requires maxDecouvert >= 0;
        requires -maxDecouvert < solde;
        ensures maxDecouvert == decouvert;
    {
        decouvert = maxDecouvert;
    }

	public void credit(double valeur)
	    requires valeur >= 0.0;
        ensures solde == old(solde) + valeur;
	{
        solde += valeur;
	}

	public void debit(double valeur)
	    requires valeur >= 0.0;
        requires valeur <= solde + decouvert;
        ensures solde >= -decouvert;
	{
        solde -= valeur;
    }
}

