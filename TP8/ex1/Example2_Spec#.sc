/*
* SVL 1617 - M. Nebut - TP vérif
* ex basique avec Spec#
*/

public class CalculAbs {

  public static int Abs(int i)
    ensures result >= 0; 	 
  {
    return i > 0 ? i : -i;
  }
}
