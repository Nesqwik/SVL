
public class Compte {
	public int solde;

    invariant solde >= 0;

    public Compte()
        ensures solde == 0;
    {
        solde = 0;
    }

	public void credit(int valeur)
	    requires valeur >= 0;
	    ensures solde == old(solde) + valeur;
	{
        solde += valeur;
	}

	public void debit(int valeur)
	    requires valeur >= 0;
	    requires valeur <= solde;
	    ensures solde >= 0;
	{
        solde -= valeur;
    }
}

