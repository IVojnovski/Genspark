import java.util.Scanner;
import java.util.Random;

public class HangMan {
	public static void main (String[] args) {
		Scanner player = new Scanner(System.in);
		String word = wordChooser(); //word the cpu will play hangman with
		String underScore = undScore(word); //makes word String into a string of its amount of characters into underscores
		String missLet = ""; //missed letters added to this string
		String repeatLet = ""; // the letters that are already missed or part of the word so that the player doesn't repeatedly do the wrong answer
		int lives = 6; //reduce lives by 1 after every incorrect guess
		
		//Rules section
		//if you guess one letter it will be compared against the word string and added to the hidden word if correct and add to the hangman if not present
		//if you guess more than one character at a time (a word guess) then it will be considered a word guess and no letters will be revealed unless you get the answer correct
		
		System.out.println("H A N G M A N !");
		System.out.println(" ");
		System.out.println("+---+");
		System.out.println(" ");
		System.out.println("    |");
		System.out.println("    |");
		System.out.println("    |");
		System.out.println(" ");
		System.out.println("   ===");
		System.out.println("WORD TO GUESS: " + underScore); // + underscores that show empty word
		System.out.println(" ");
		System.out.println("Missed Letters: "); //+ missLet
		System.out.println("Guess a Letter!");
		
		compare(player.nextLine(), word, underScore, missLet, repeatLet, lives);
		
		// add letter to missed letters string if not present in word, also add a new part to the hangman string
		// if present in word, replace underscore with the letter guessed
		// need to make code that makes it so that it detects the amount of characters in a word and makes a string that can be edited to replace the underscores with the
		// appropriate letter(s).
		
		//receive input from player!
		//print the players input and put into the function that
		//dictates whether or not the character is in the String
		
		player.close();
	}
	static String compare (String input, String wrd, String und, String misLet, String repLet, int life) {
		//character guess
		//take the input as a string then isolate the character if the guess is
		//no more than one letter and if it detects the word is more than one
		//character then make an if statement that compares the entire word to the
		//entire String and if wrong subtract one from lives by changing the boolean check
		
		if (input.length() > 1 && wrd.contains(input)) {
			//complete word guess statement
		}
		if (input.length() <= 1 && wrd.contains(input)) {
			//one character guess
			char[] arr = wrd.toCharArray();
			String ans = "";
			
			for (int i = 0;i < arr.length;i++) {
				if (arr[i] + "" == input) {
					ans += input;
				}
				else {
					ans += " _";
				}
			}
		}
		
		//word guess
		//if word contains all letters of applicable word == win!
		
		return "";
	}
	
	static String undScore (String x) {
		char[] arr = x.toCharArray();
		String und = "_ ";
		String ret = "";
		
		for (int i = 0;i <= arr.length;i++) {
			ret += und;
		}
		
		return ret;
	}
	
	static String wordChooser () {
		Random rand = new Random();
		int upperbound = 10;
		int random = rand.nextInt(upperbound);
		
		switch (random) {
		case 0:
			return "cat";
		case 1:
			return "dog";
		case 2:
			return "fur";
		case 3:
			return "max";
		case 4:
			return "min";
		case 5:
			return "list";
		case 6:
			return "more";
		case 7:
			return "thing";
		case 8:
			return "them";
		case 9:
			return "four";
		case 10:
			return "lion";
		default:
			return "iiiiiiiiiiiiiiiiiiiiiiii";
		}
	}
}
