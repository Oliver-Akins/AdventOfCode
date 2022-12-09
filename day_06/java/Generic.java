package day_06.java;

import java.io.FileNotFoundException;
import java.util.Scanner;

import jlib.FileSystem;
import jlib.Sequence;

class Generic {
	static Integer bufferSize;

	public static void main(String[] args) {
		if (args.length < 2) {
			System.out.println("Not enough arguments");
			return;
		}

		bufferSize = Integer.parseInt(args[1]);

		Scanner s;
		try {
			s = FileSystem.readFile(args[0]);
		} catch (FileNotFoundException e) {
			System.out.println("Can't find the file");
			return;
		}

		while (s.hasNextLine()) {
			String line = s.nextLine();
			Sequence<Character> buffer = new Sequence<>(bufferSize);

			// Ensure the line has enough characters to make a marker
			if (line.length() < 4) {
				System.out.println("Not long enough to get a marker");
			}

			// Find the marker in the data
			for (int i = 0; i < line.length(); i++) {
				buffer.add(line.charAt(i));
				if (buffer.size() == bufferSize && buffer.isUnique()) {
					System.out.println("Found marker at character " + (i + 1));
					break;
				}
			}
		}
	}
}
