class Sqrt {

  int sqrt(int x)
    requires x >= 0;

    ensures result >= 0;
    ensures result * result <= x;
    ensures (result + 1) * (result + 1) > x;
  {
    int i = 0;

    while((i + 1) * (i + 1) <= x)
     invariant i * i <= x;
     invariant i >= 0;
    {
      i++;
    }

    return i;
  }
}
