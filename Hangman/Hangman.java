import java.util.*;
import java.util.concurrent.TimeUnit;
import java.io.*;
public class Hangman {
//TODO: prepare different responses for game stats depending on percentage and how many games were played
//	format stats so percentage has no decimals (or 2 decimals at most?)

	//variables defined in prepareNewGame()
	public static int numberInWrong;
	public static int wrongGuesses;
	public static String currentGuess;
	public static char[] wrongLetters;
	public static String answer;
	public static boolean hasWon;
	public static final String[] BODY_PARTS = {"0", "--", "|", "--", "/", "\\"};
	
	public static float gamesPlayed = 0;
	public static float gamesWon = 0;

	public static Scanner userInput = new Scanner(System.in);
	public static ArrayList<String> words = new ArrayList<>();

	public static void drawHang() {
		String[] bodyOn = {" ", " ", " ", " ", " ", " "};
		for (int c = 0; c < wrongGuesses; c++) {
			bodyOn[c] = BODY_PARTS[c];
		}
		System.out.print("\n      ____\t");
		for (int i = 0; i < wrongLetters.length; i++) {
			System.out.print(wrongLetters[i] + " ");
		}
		System.out.println("\n      |   |");
		System.out.println("      |   " + bodyOn[0]);
		System.out.println("      | " + bodyOn[1] + bodyOn[2] + bodyOn[3]);
		System.out.println("      |  " + bodyOn[4] + " " +  bodyOn[5]);
		System.out.println("    __|__");
		System.out.println("    |    |");
		System.out.println("\n " + currentGuess);
	}
	
	public static boolean checkGuess(String str) {
		boolean returnBoo = false;
		if (str.length() == 1) {
			char strChar = str.toCharArray()[0];
			for (int i = 0; i < answer.length(); i++) {
				if (answer.charAt(i) == strChar) {
					char[] currentCharGuess = currentGuess.toCharArray();
					currentCharGuess[i] = strChar;
					currentGuess = new String(currentCharGuess);
					returnBoo = true;
				}
			}
			if (currentGuess.equals(answer)) {
				hasWon = true;
			}
			if (!returnBoo) {
				boolean add = true;
				//checks if letter guess has already been guessed
				for (int i = 0; i < numberInWrong; i++) {
					if (strChar == wrongLetters[i]) {
						add = false;
					}
				}
				if (add) {
					wrongLetters[numberInWrong] = strChar;
					numberInWrong++;
				}
			}
			return returnBoo;
		} else {
			if (str.length() == answer.length()) {
				if (str.equalsIgnoreCase(answer)) {
					returnBoo = true;
					hasWon = true;
					currentGuess = answer;
				}
			}
			return returnBoo;
		}
	}
	
	public static void runGame() {
		String input = "";
		do {
			drawHang();
			System.out.print("Enter your guess: ");
			String userGuess = userInput.nextLine();
//			System.out.println("userGuess: " + userGuess);
			boolean goodOrBad = checkGuess(userGuess);
			if (!goodOrBad) {
				wrongGuesses++;
			}
		} while (wrongGuesses < 6 ^ hasWon == true);
		if (hasWon) {
			drawHang();
			System.out.println("\nYay! You won!\n");
			gamesWon++;
			pause(1);
		} else {
			drawHang();
			System.out.println("\nSadness... you have been hung...");
			System.out.println("\nAnswer: " + answer + "\n");
			pause(1);
		}
	}
	
	public static void prepareNewGame() {
		numberInWrong = 0;
		wrongGuesses = 0;
		currentGuess = "";
		wrongLetters = new char[7];
		hasWon = false;
		
		//chooses random word from words Arraylist
		double randomWordChooser;
		randomWordChooser = Math.round(Math.random() * (words.size()-1));
		answer = words.get((int)randomWordChooser);		
		
		//gives currentGuess number of -'s equal to letters in word
		for (int i = 0; i < answer.length(); i++) {
			currentGuess += "-";
		}
	}
	
	public static void pause(int seconds) {
			try {
				TimeUnit.SECONDS.sleep(seconds);
			} catch (InterruptedException ie) {
				ie.printStackTrace();
			}

	}

	public static void printStats() {
		
		System.out.println("Number of games played: " + (int)gamesPlayed);
		System.out.println("Percentage of games won: " + (gamesWon/gamesPlayed)*100 + "%");
	}

	public static void main(String[] args) {
		
		//initializes word array from words.txt
		try (Scanner readFile = new Scanner(new File("words.txt"))) {
			while(readFile.hasNextLine()) {
				words.add(readFile.nextLine());
			}
		} catch (FileNotFoundException fnfe) {
			fnfe.printStackTrace();
		}

		//actual workspace of program
		System.out.println("Welcome to hangman! In this game, guesses can consist of a single letter or");
		System.out.println("the entire word. But be careful! If you enter a word that does not have the");
		System.out.println("same number of letters as the answer, the program will automatically count you wrong.");
		System.out.println("Also, be sure to leave no spaces in your word when you guess it.");
		System.out.println("Have fun!\n");
		boolean keepPlaying = false;

		pause(6);

		do {
			prepareNewGame();
			runGame();
			gamesPlayed++;
			
			//removes old answer from the arraylist
			if (!(answer == null)) {
				words.remove(answer);
			}
			
			//exits the program if there are no words left
			if (words.size() == 0) {
				System.out.println("Wow, you've used all the words! Thanks for playing!");
				pause(2);
				break;
			}

			System.out.print("Do you want to play again? (y/n): ");
			boolean impudence = false;
			do {
				try {
					char playOrNo = userInput.nextLine().charAt(0);
					if (playOrNo == 'y' || playOrNo == 'Y') {
						keepPlaying = true;
						impudence = false;
					} else if (playOrNo == 'n' || playOrNo == 'N') {
						keepPlaying = false;
						System.out.println("\nOkay! Thanks for playing!\n");
						printStats();
						pause(5);
						impudence = false;
					} else {
						System.out.print("Please enter a \"y\" or an \"n\": ");
						impudence = true;
					}
				} catch (StringIndexOutOfBoundsException sioobe) {
					System.out.print("Please enter a \"y\" or an \"n\": ");
					impudence = true;
					continue;
				}
			} while (impudence);
			
		} while (keepPlaying);

		
		userInput.close();
	}
}
