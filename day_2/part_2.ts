// @ts-ignore
import { readFileSync } from "fs";


let data: string = readFileSync("input", "utf-8");


let ribbon_sum: number = 0;

for (var line of data.split(`\n`)) {
	let dimensions: string[] = line.split("x", 3);

	let l = parseInt(dimensions[0]);
	let w = parseInt(dimensions[1]);
	let h = parseInt(dimensions[2]);

	let min_perimeter: number = Math.min(
		l+l+w+w,
		l+l+h+h,
		w+w+h+h
	);

	let volume: number = l * w * h;

	ribbon_sum = ribbon_sum + min_perimeter + volume;
};


console.log(`Ribbon Length Needed: ${ribbon_sum}`);