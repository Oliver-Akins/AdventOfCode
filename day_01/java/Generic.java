import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Generic {
	/*
	 * Expects two command line arguments:
	 * - The file name to load
	 * - The number of top values to sum together
	 */
	public static void main (String[] args) {
		Scanner f;
		try {
			f = Generic.readFile(args[0]);
		} catch (FileNotFoundException e) {
			System.out.println("File not found, stopping execution");
			return;
		}

		Integer count = Integer.parseInt(args[1]);

		ArrayList<Integer> top = new ArrayList<Integer>();
		Integer runningSum = 0;
		while (f.hasNextLine()) {
			String l = f.nextLine();
			if (l.equals("")) {
				if (top.size() < count) {
					top.add(runningSum);
				}
				else if (Collections.min(top) < runningSum) {
					top.add(runningSum);
					top.removeIf(x -> x <= Collections.min(top));
				}
				runningSum = 0;
			} else {
				runningSum = runningSum + Integer.parseInt(l);
			}
		}
		f.close();


		Collections.sort(top, Collections.reverseOrder());
		System.out.print(
			"The largest " + count + " values are: "
			+ top.subList(0, count).toString()
			+ " totalling: "
		);
		Integer sum = 0;
		for (int i = 0; i < count; i++) {
			sum = sum + top.get(i);
		}
		System.out.println(sum);
	}

	private static Scanner readFile(String file) throws FileNotFoundException {
		File f = new File(file);
		Scanner s = new Scanner(f);
		return s;
	}
}