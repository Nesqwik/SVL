/*
* SVL 1617 - M. Nebut
* démo pour JML sur rise4fun
*/

public class Score {
 
    //@ public invariant score1 >= 0;
    //@ public invariant score2 >= 0;
   
    public int score1;
    public int score2;

    //@ ensures score1 == 0;
    //@ ensures score2 == 0;
    public Score()  {
	score1 = 0;
	score2 = 0;
    }

    //@ requires num_joueur == 1 || num_joueur == 2;
    //@ requires points > 0;
    //@ ensures num_joueur == 1 ==> score1 == \old(score1) + points;
    //@ ensures num_joueur == 2 ==> score2 == \old(score2) + points;
    public void ajouter_points(int num_joueur, int points)
    {
      if (num_joueur == 1) {
         score1 += points;         
         score1 -= 1000; //ça passe
         score1 += 1000;
      }
      else
         score2 += points;
    }

    // cette spec est fausse, cf cas exequo
    //@ ensures score1 > score2 <==> \result == 1;
    //@  ensures score2 > score1 <==> \result == 2; 
    public int gagnant()
      {
        if (score1 > score2)
           return 1;
        else
           return 2;
      }
}
