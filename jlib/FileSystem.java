package jlib;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileSystem {
	public static Scanner readFile(String path) throws FileNotFoundException {
		File f = new File(path);
		return new Scanner(f);
	}
}
