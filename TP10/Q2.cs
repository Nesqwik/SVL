class Q2 {

  int nb5(int[] tab)
    ensures result == sum{int n in (0:tab.Length); (tab[n] == 5 ? 1 : 0)};
  {
    int cpt = 0;
    for(int i = 0 ; i < tab.Length ; i++)
     invariant i <= tab.Length;
     invariant cpt == sum{int n in (0:i); (tab[n] == 5 ? 1 : 0)};
    {
      if(tab[i] == 5) {
        cpt++;
      }
    }
    return cpt;
  }
}
