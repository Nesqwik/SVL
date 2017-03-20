/*
* SVL 1617 - M. Nebut
* démo pour Spec# sur rise4fun
*/

class Score {
 
  invariant score1 >= 0;
  invariant score2 >= 0;
   
  public int score1;
  public int score2;
  
  public Score()
     ensures score1 == 0;
     ensures score2 == 0;
  {
    score1 = 0;
    score2 = 0;
  }
  
  public void ajouter_points(int num_joueur, int points)
    requires num_joueur == 1 || num_joueur == 2;
    requires points > 0;
    ensures num_joueur == 1 ==> score1 == old(score1) + points;
    ensures num_joueur == 2 ==> score2 == old(score2) + points;
    {
      if (num_joueur == 1) {
         score1 += points;
         /* expose (this)  // pour montrer le traitement des invariants
         {score1 -= 1000;
         score1 += 1000;} */
      }
      else
         score2 += points;
    }
    
    public int gagnant()
    // cette spec est fausse, cf cas exequo
      ensures score1 > score2 <==> result == 1;
      ensures score2 > score1 <==> result == 2; 
      {
        if (score1 > score2)
           return 1;
        else
           return 2;
      }
}

