import java.util.ArrayList;
import java.util.List;

/**
 * Tour<br/>
 * Created by dalencourt on 13/03/17.
 */
public class Tour {
    private /*@ spec_public @*/ List<Disque> tour;

    //@ public invariant this.tour != null;
    //@ public invariant (\forall int i; 0 <= i && i < tour.size() - 1; tour.get(i).getTaille() > tour.get(i+1).getTaille());


    public Tour() {
        this.tour = new ArrayList<Disque>();
    }

    //@ requires taille > 0;
    //@ ensures this.tour.size() == taille;
    //@ ensures (\forall int i; 0 <= i && i < tour.size() - 1; tour.get(i).getTaille() - 1 == tour.get(i+1).getTaille());
    public void initTour(int taille){
        for(int i = taille; 0 < i; i--){
            tour.add(new Disque(i));
        }
    }

    //@ requires disque != null;
    //@ signals (DisqueTropFatException e) disque.getTaille() < this.tour.get(this.tour.size() - 1).getTaille();
    public void empile(Disque disque) throws DisqueTropFatException {
        if(disque.getTaille() < this.tour.get(this.tour.size()-1).getTaille()){
            throw new DisqueTropFatException();
        }
        tour.add(disque);
    }

    //@ signals (PileVideException e) this.tour.size() == 0;
    //@ ensures \result == \old(this.tour.get(this.tour.size() - 1));
    public Disque depile() throws PileVideException {
        if(this.tour.size() == 0){
            throw new PileVideException();
        }
        return tour.remove(tour.size() - 1);
    }

    public List<Disque> getTour() {
        return tour;
    }

    public void setTour(final List<Disque> tour) {
        this.tour = tour;
    }
}
