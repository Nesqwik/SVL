/*
* SVL 1617 - M. Nebut - TP vérif
* ex basique avec JML
*/

class Example1 {
  public int x;

  //@ requires y > 0;
  //@ ensures \old(x) < x;
  void inc(int y) {
    x += y;
  }
}
