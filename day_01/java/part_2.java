import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Part2 {
	public static void main (String[] args) {
		Scanner f;
		try {
			f = Part2.readFile(args[0]);
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

		Collections.sort(sums, Collections.reverseOrder());
		System.out.print(
			"The largest three values are: "
			+ sums.subList(0, 3).toString()
			+ " totalling: "
		);
		System.out.println(sums.get(0) + sums.get(1) + sums.get(2));
	}

	private static Scanner readFile(String file) throws FileNotFoundException {
		File f = new File(file);
		Scanner s = new Scanner(f);
		return s;
	}
}
