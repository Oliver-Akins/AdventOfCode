import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

class Part1 {
	public static void main (String[] args) {
		Scanner f;
		try {
			f = Part1.readFile(args[0]);
		} catch (FileNotFoundException e) {
			System.out.println("File not found, stopping execution");
			return;
		}

		ArrayList<Integer> sums = new ArrayList<Integer>();
		Integer runningSum = 0;
		while (f.hasNextLine()) {
			String l = f.nextLine();
			if (l.equals("")) {
				sums.add(runningSum);
				runningSum = 0;
			} else {
				runningSum = runningSum + Integer.parseInt(l);
			}
		}
		f.close();

		Iterator<Integer> i = sums.iterator();
		Integer largest = Integer.MIN_VALUE;
		while (i.hasNext()) {
			Integer sum = i.next();
			if (sum > largest) {
				largest = sum;
			}
		}
		System.out.print("The largest value is: ");
		System.out.println(largest);
	}

	private static Scanner readFile(String file) throws FileNotFoundException {
		File f = new File(file);
		Scanner s = new Scanner(f);
		return s;
	}
}