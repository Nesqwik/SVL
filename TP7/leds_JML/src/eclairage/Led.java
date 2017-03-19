/*
SVL 16-17 M. Nebut
ex de spéc JML - CTD7 prog par contrats.
*/

package eclairage;

public class Led {

    private /*@ spec_public @*/ boolean allumee;

    //@ ensures ! allumee;
    public Led() {
	this.allumee = false;
    }

    //@ ensures allumee;
    public void allumer() {
	this.allumee = true;
    }

    //@ ensures ! allumee;
    public void eteindre() {
	this.allumee = false;
    }


    public static void main(String args[]) throws Exception {
	Led led = new Led();
	led.eteindre();
	led.allumer();
    }
    
}
