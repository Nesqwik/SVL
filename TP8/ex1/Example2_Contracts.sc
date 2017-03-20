/*
* SVL 1617 - M. Nebut - TP vérif
* ex basique avec Code Contracts
*/

using System.Diagnostics.Contracts;

public class CalculAbs {

  public static int Abs(int i) {
    Contract.Requires(i != -2147483648);
    Contract.Ensures(Contract.Result<int>() >= 0); 	 
    return i > 0 ? i : -i;
  }
}
