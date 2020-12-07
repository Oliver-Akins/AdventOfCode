// @ts-ignore
import { readFileSync } from "fs";


let data: string = readFileSync("input", "utf-8");

let surface_area_sum: number = 0;

for (var dimensions of data.split("\n")) {
	let dimension_array: string[] = dimensions.split("x");

	let l: number = parseInt(dimension_array[0]),
		w: number = parseInt(dimension_array[1]),
		h: number = parseInt(dimension_array[2]);

	let surface_area: number = (2*l*w + 2*l*h + 2*h*w + Math.min(l*w, l*h, h*w));

	surface_area_sum = surface_area_sum + surface_area;
};

console.log(`Total Surface Area Needed Of Wrapping Paper: ${surface_area_sum}`);