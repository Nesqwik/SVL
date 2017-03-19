/*
SVL 16-17 M. Nebut
ex de spéc JML - CTD7 prog par contrats.
 */
package restaurant_entreprise;

public class DebitException extends Exception {

    // rajouté car sinon JML râle pour violation invariant de Throwable
    //@ public represents _stackTrace <- this.getStackTrace();
    
}
