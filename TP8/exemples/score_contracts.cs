/*
* SVL 1617 - M. Nebut
* démo pour CodeContracts sur rise4fun
*/

using System;
using System.Diagnostics.Contracts;

class Score {
 
  [ContractInvariantMethod]
     void ObjectInvariant () {  
       Contract.Invariant(score1 >= 0);
       Contract.Invariant(score2 >= 0);
     }
     
  public int score1;
  public int score2;
  
  public Score() {
     Contract.Ensures(score1 == 0);
     Contract.Ensures(score2 == 0);
  
    score1 = 0;
    score2 = 0;
  }
  
  public void ajouter_points(int num_joueur, int points){
    Contract.Requires(num_joueur == 1 || num_joueur == 2);
    Contract.Requires(points > 0);
    Contract.Ensures(! (num_joueur == 1) || (score1 == Contract.OldValue(score1) + points)); // num_joueur == 1 ==> score1 == old(score1) + points;
    Contract.Ensures(! (num_joueur == 2) || (score2 == Contract.OldValue(score2) + points)); // num_joueur == 2 ==> score2 == old(score2) + points;
    
      if (num_joueur == 1)
         score1 += points;
      else
         score2 += points;
    }
    
    public int gagnant() {
      Contract.Ensures((score1 > score2) == (Contract.Result<int>() == 1));
      Contract.Ensures((score2 > score1) == (Contract.Result<int>() == 2));
      
        if (score1 > score2)
           return 1;
        else
           return 2;
      }
}
