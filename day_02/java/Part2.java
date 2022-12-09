package day_02.java;

import java.io.FileNotFoundException;
import java.util.*;

import jlib.FileSystem;

public class Part2 {
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
			Integer round = determineScore(
				l.charAt(0),
				l.charAt(l.length() - 1)
			);
			points = points + round;
		}
		System.out.println(points + " points");
	}

	/*
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


	public static int winAgainst(int choice) {
		int value = choice + 1;
		if (value > 3) {
			value = 1;
		}
		return value;
	};

	public static int loseAgainst(int choice) {
		int value = choice - 1;
		if (value < 1) {
			value = 3;
		}
		return value;
	}

	public static Integer determineScore(Character opponent, Character desiredResult) {
		int opposing = (int)opponent - 64;
		switch (desiredResult) {
			case 'X':
				return loseAgainst(opposing);
			case 'Y':
				return opposing + 3;
			case 'Z':
				return winAgainst(opposing) + 6;
		}
		return 0;
	}
}