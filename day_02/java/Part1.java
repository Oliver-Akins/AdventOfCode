package day_02.java;

import java.io.FileNotFoundException;
import java.util.*;

import jlib.FileSystem;

public class Part1 {
	public static void main(String[] args) {
		if (args.length < 1) {
			System.out.println("Not enough args");
			return;
		};
		Scanner s;
		try {
			s = FileSystem.readFile(args[0]);
		} catch (FileNotFoundException e) {
			System.out.println("Can't find that file");
			return;
		}

		Integer points = 0;
		while (s.hasNextLine()) {
			String l = s.nextLine();
			Integer round = Part1.determineScore(
				l.charAt(l.length() - 1),
				l.charAt(0)
			);
			points = points + round;
		}
		System.out.println(points + " points");
	}

	/**
	 * Determines if we win or the opponent wins in a game of Rock Paper Scissors
	 *
	 * A = Rock
	 * B = Paper
	 * C = Scissors
	 *
	 * X = Rock
	 * Y = Paper
	 * Z = Scissors
	 *
	 *      Paper
	 *     /     ^
	 *    /       \
	 *   v         \
	 * Rock --> Scissors
	 *
	 */
	public static boolean isWin(Character me, Character opponent) {
		if ( me.equals(opponent) ) {
			return false;
		}
		else if (opponent.equals('A')) {
			return me.equals('Y');
		} else if (opponent.equals('B')) {
			return me.equals('Z');
		} else {
			return me.equals('X');
		}
	}

	public static Integer determineScore(Character me, Character opponent) {
		Integer choice = (int)me - 87;

		if (choice == ((int)opponent - 64)) {
			return 3 + choice;
		}

		if (Part1.isWin(me, opponent)) {
			return 6 + choice;
		}
		return choice;
	}
}