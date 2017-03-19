/*
SVL 16-17 M. Nebut
ex de spéc JML - CTD7 prog par contrats.
*/

package eclairage;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Rampe {

    private /*@ spec_public @*/ List<Led> les_leds;

    //@ ensures les_leds == leds;
    public Rampe(List<Led> leds) {
	this.les_leds = leds;
    }

    // non executable
    // @ ensures (\forall Led led; les_leds.contains(led); ! led.allumee);
    //@ ensures (\forall int i; 0 <= i && i < les_leds.size(); ! les_leds.get(i).allumee);
    public void eteindre() {
	for (Led led : this.les_leds)
	    led.eteindre();
    }

    // non executable
    // @ ensures (\exists Led led; les_leds.contains(led); led.allumee);
    //@ ensures (\exists int i; 0 <= i && i < les_leds.size();  les_leds.get(i).allumee);
    public void allumer_led_aleatoirement(Random generateur) {
	int indice = generateur.nextInt(this.les_leds.size());
	this.les_leds.get(indice).allumer();
    }
    
    public static void main(String args[]) throws Exception {
	Led led1 = new Led();
	Led led2 = new Led();
	Led led3 = new Led();
	led1.allumer();
	led3.allumer();
	Rampe rampe = new Rampe(new ArrayList<Led>(Arrays.asList(led1, led2, led3)));
	rampe.eteindre();
	Random generateur = new Random();
	rampe.allumer_led_aleatoirement(generateur);
    }

}
