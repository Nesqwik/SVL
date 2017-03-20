using System;
using System.Diagnostics.Contracts;

public class Compte {
	public int solde;
	public int decouvert;

    invariant solde >= -decouvert;
    invariant decouvert >= 0 ;

    public Compte()
        ensures solde == 0;
        ensures decouvert == 0;
    {
        decouvert = 0;
        solde = 0;
    }


    public void autoriserDecouvert(int maxDecouvert)
        requires maxDecouvert >= 0;
        requires -maxDecouvert < solde;
        ensures maxDecouvert == decouvert;
    {
        decouvert = maxDecouvert;
    }

	public void credit(int valeur)
	    requires valeur >= 0;
        ensures solde == old(solde) + valeur;
	{
        solde += valeur;
	}

	public void debit(int valeur)
	    requires valeur >= 0;
        requires valeur <= solde + decouvert;
        ensures solde >= -decouvert;
	{
        solde -= valeur;
    }
}

