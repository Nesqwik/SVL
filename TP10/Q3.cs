class Q3 {

  int indexOfNeg(int[] tab)
    ensures forall{int n in (0:tab.Length); tab[n] > 0} ==> (result == -1);
    ensures exists{int n in (0:tab.Length); tab[n] < 0} ==> tab[result] < 0;
    ensures forall{int n in (0:result); tab[n] > 0};
  {
    for(int i = 0 ; i < tab.Length ; i++)
     invariant i <= tab.Length;
     invariant forall{int n in (0:i + 1); tab[n] > 0};
    {
      if(tab[i] < 0) return i;
    }
    return -1;
  }
}
