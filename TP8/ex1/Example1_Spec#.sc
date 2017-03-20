/*
* SVL 1617 - M. Nebut - TP vérif
* ex basique avec Spec#
*/

class Example1 {
  int x;
  
  void Inc(int y)
    requires y > 0;
    ensures old(x) < x;
  {
    x += y;
  }
}
