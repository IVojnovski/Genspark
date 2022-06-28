import java.util.Random;
import java.util.Scanner;

public class GuessTheNumber {
	
	public static void main(String[] args) {
		GuessTheNumberGame();
		
		switch (GuessTheNumberGame()) {
		case "y":
			GuessTheNumberGame();
		case "n":
			System.exit(0);
		default:
			System.out.println("invalid choice!");
			System.exit(0);
		}
	}
	
	public static String GuessTheNumberGame() {
		//need to output player input in bold !! (like in DragonCave as well

		Random rand = new Random();
		Scanner player = new Scanner(System.in);
		Scanner replay = new Scanner(System.in);
		
		String playerName;
		int cpuNumber = rand.nextInt(1, 20);
		int playerGuess;
		String replayGame;
		
		System.out.println("Hello! What is your name?");
		
		playerName = player.nextLine();
		//detects name input by player
		
		System.out.println("Well, " + playerName + ", I am thinking of a number between 1 and 20.");
		System.out.println("You have 6 tries to guess my number!");
		
		//playerGuess = player.nextInt();
		//detects integer guess from 1-20 and makes you lose if you guess outside of the range
		
		for (int i = 1; i <= 6; i++) {
			System.out.println("Take a guess.");
			playerGuess = player.nextInt();
			
			if(playerGuess > cpuNumber) {
				System.out.println(">> " + playerGuess);
				System.out.println("Your guess is too high.");
				System.out.println("You have " + (6 - i) + " tries left!");
			}
			if(playerGuess < cpuNumber) {
				System.out.println(">> " + playerGuess);
				System.out.println("Your guess is too low.");
				System.out.println("You have " + (6 - i) + " tries left!");
			}
			if(playerGuess > 20 || playerGuess < 1) {
				System.out.println(">> " + playerGuess);
				System.out.println("Your guess is out of bounds.");
				System.out.println("You have " + (6 - i) + " tries left!");
			}
			if(playerGuess == cpuNumber) {
				System.out.println("Good job, " + playerName + "! You guessed my number in " + i + " guesses!");
				System.out.println("Would you like to play again? (y or n)");
				
				replayGame = replay.nextLine();
				
				switch(replayGame) {
				case "y":
					return replayGame;
				case "n":
					return replayGame;
				default:
					return null;
				}
			}
		}
		
		System.out.println("You ran out of tries!");
		System.out.println("Would you like to play again? (y or n)");
		
		replayGame = replay.nextLine();
		
		switch(replayGame) {
		case "y":
			return replayGame;
		case "n":
			return replayGame;
		default:
			return null;
		}
	}

}
