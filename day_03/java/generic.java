package day_03.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class generic {
	public static void main(String[] args) {
		if (args.length < 2) {
			System.out.println("Not enough args");
			return;
		};
		Scanner s;
		try {
			s = generic.readFile(args[0]);
		} catch (FileNotFoundException e) {
			System.out.println("Can't find that file");
			return;
		}

		Boolean part2 = args[1].equals("2");
		Integer total = 0;
		while (s.hasNextLine()) {
			String c;
			if (part2) {
				c = generic.p2(s);
			} else {
				c = generic.p1(s);
			}
			Integer v = generic.priority(c);
			total = total + v;
		}
		System.out.println(total);
	}

	public static String p1(Scanner file) {
		String l = file.next();
		Integer mid = l.length() / 2;
		return generic.intersect(
			l.substring(0, mid),
			l.substring(mid)
		);
	}

	public static String p2(Scanner file) {
		String l1 = file.next();
		String l2 = file.next();
		String l3 = file.next();
		return generic.intersect( l1, l2, l3 );
	}

	public static String intersect(String... s) {
		Set<Character> intersection = generic.toSet(s[0]);
		for (int i = 1; i < s.length; i++) {
			intersection.retainAll(generic.toSet(s[i]));
		}
		if (intersection.size() == 1) {
			return intersection.toArray()[0].toString();
		}
		return "";
	}

	public static Set<Character> toSet(String s) {
		Set<Character> result = new HashSet<Character>();
		for (int i = 0; i < s.length(); i++) {
			result.add(s.charAt(i));
		}
		return result;
	}

	public static Integer priority(String s) {
		char c = s.charAt(0);
		Integer v = (int) c;
		if (Character.isLowerCase(c)) {
			return v - 96;
		} else if (Character.isUpperCase(c)) {
			return v - 38;
		} else {
			return 0;
		}
	}

	public static Scanner readFile(String path) throws FileNotFoundException {
		File f = new File(path);
		return new Scanner(f);
	}
}