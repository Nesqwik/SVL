/**
 * Disque <br/>
 * Created by dalencourt on 13/03/17.
 */
public class Disque {
    private /*@ spec_public @*/ int taille;

    //@ public invariant this.taille > 0;


    /**
     * Constructor
     * @param taille
     */
    //@ requires taille > 0;
    public Disque(final int taille) {
        this.taille = taille;
    }

    public int getTaille() {
        return taille;
    }

    public void setTaille(final int taille) {
        this.taille = taille;
    }
}
