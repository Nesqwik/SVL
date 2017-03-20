/*
* SVL 1617 - M. Nebut - TP vérif
* ex basique avec JML
*/

public class CalculAbs {

    //@ ensures \result >= 0; 	 
  public static int abs(int i) {
    return i > 0 ? i : -i;
  }
}
