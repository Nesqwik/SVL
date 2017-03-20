using System;
/*
* SVL 1617 - M. Nebut - TP vérif
* ex basique avec CodeContracts
*/

using System.Diagnostics.Contracts;

public class Example1 {
  int x;

  public void Inc(int y) {
    Contract.Requires(y > 0);
    Contract.Ensures(Contract.OldValue(x) < x);
    x += y;
  }
}
