import java.util.Scanner;

public class DragonCave {
	
	public static void main(String[] args) {
		/* main comment section
		 * comment like a stranger is playing the game!
		 * can't make text output in bold in eclipse :(
		 * make it so that choice2 isnt case sensitive and shows bold in above print statement
		 * equalsIgnoreCase!!!! method would allow me to take input in a non-case sensitive way!
		 * put try catch exception handling wherever input is received (for example the default methods!!)
		 * make unit tests in the tests folder of every project 
		 * When code defaults try catch should be used to throw an exception and allow the input to be re-input*/
		dragonCaveScenario();
	}
	
	public static String dragonCaveScenario() {
		Scanner player = new Scanner(System.in);
		
		int choice1 = 0;
		String choice2;
		
		System.out.println("You are in a land full of dragons. In front of you,");
		System.out.println("you see two caves. In one cave, the dragon is friendly");
		System.out.println("and will share his treasure with you. The other dragon");
		System.out.println("is greedy and hungry and will eat you on sight.");
		System.out.println(">> Which cave will you go into? (1 or 2)");
		
		try {
			choice1 = player.nextInt();
		}
		catch (Exception e){
			System.out.println("Invalid answer, please re-run the code and try again");
			player.close();
			return null;
		}
		
		System.out.println(">> " + String.valueOf(choice1));
		
		switch(choice1) {
		
		case 1:
			System.out.println("You approach the cave...");
			System.out.println("It is dark and spooky...");
			System.out.println("A large dragon jumps out in front of you! He opens his jaws and...");
			System.out.println("Gobbles you down in one bite!");
			player.close();
			return "!! YOU ARE DEAD !!";
			
		case 2: 
			System.out.println("You approach the cave...");
			System.out.println("It is dark and spooky...");
			System.out.println("A large dragon jumps out in front of you! He opens his jaws and...");
			System.out.println("You see a key stuck in one of the dragon's teeth!");
			System.out.println(">> Do you grab the key? (yes or no)");
			break;
		}
		
		choice2 = player.next();
		
		System.out.println(">> " + choice2);
			
		switch(choice2) {
		
		case "yes":
			System.out.println("You cautiously approach the dragon's mouth...");
			System.out.println("The dragon's somewhat steady breathing is somewhat reassuring...");
			System.out.println("You tug at the key that is loosely hanging off of the dragon's tooth!");
			System.out.println("You have the key!");
			System.out.println("The dragon's mouth shuts! ...");
			System.out.println("The dragon darts up and swiftly changes direction...");
			System.out.println("Revealing a lone chest!");
			System.out.println("You open the chest and see that it is full of valuable jewels and gold!");
			player.close();
			return "!! YOU WIN !!";
			
		case "no":
			System.out.println("You are stricken with fear and refuse to approach!");
			System.out.println("You try to slowly backtrack to the entrance...");
			System.out.println("The dragon seems to have taken this as a sign of disrespect!");
			System.out.println("The dragon takes a deep breath in and exhales a stream of flames!!!");
			System.out.println("You are burnt to a pile of ashes!");
			player.close();
			return "!! YOU ARE DEAD !!";
			
		default:
			System.out.println("Invalid answer, please re-run the code and try again");
		    player.close();
		    return "please reload the code to retry";
		}
	}
}
