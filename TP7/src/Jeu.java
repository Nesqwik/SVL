import java.util.ArrayList;
import java.util.List;

/**
 * Jeu<br/>
 * Created by dalencourt on 13/03/17.
 */
public class Jeu {
    private /*@ spec_public @*/ List<Tour> tourList;

    //@ public invariant this.tourList != null;
    //@ public invariant this.tourList.size() >= 3;


    //@ requires size >= 3;
    //@ requires nbDisque > 0;
    public Jeu(final int size, final int nbDisque) {
        this.tourList = new ArrayList<Tour>(size);
        for(int i = 0; i < size; i++){
            this.tourList.add(new Tour());
        }
        this.tourList.get(0).initTour(nbDisque);
    }

    public List<Tour> getTourList() {
        return tourList;
    }

    //@ requires i < tourList.size();
    //@ requires i >= 0;
    //@ ensures \result == tourList.get(i);
    public Tour getTour(int i) {
        return tourList.get(i);
    }

    //@ requires tourList != null;
    //@ requires tourList.size() >= 3;
    public void setTourList(final List<Tour> tourList) {
        this.tourList = tourList;
    }

    //@ requires from >= 0;
    //@ requires from <= tourList.size() - 1;
    //@ requires to >= 0;
    //@ requires to <= tourList.size() - 1;
    //@ requires tourList.get(from).getTour().size() > 0;
    // ensures \old(tourList).get(from).getTour().size() == (tourList.get(from).getTour().size() - 1);
    // ensures \old(tourList).get(to).getTour().size() == (tourList.get(to).getTour().size() + 1);
    public void switchDisque(int from, int to) throws PileVideException, DisqueTropFatException {
        getTour(to).empile(getTour(from).depile());
    }

    public static void main (String[] args){
        Jeu jeu = new Jeu(3,3);

        try {
            jeu.switchDisque(0, 2);
            jeu.switchDisque(0, 1);
            jeu.switchDisque(2, 1);
            jeu.switchDisque(0, 2);
            jeu.switchDisque(1, 0);
            jeu.switchDisque(1, 2);
            jeu.switchDisque(0, 2);
        } catch (PileVideException e) {
            e.printStackTrace();
        } catch (DisqueTropFatException e) {
            e.printStackTrace();
        }
    }

}
