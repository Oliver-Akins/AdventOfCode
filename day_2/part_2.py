ribbon_sum = 0


with open("input", "r") as data:


	for line in data:
		dimensions = line.split("x")
		l, w, h = [int(x) for x in dimensions]

		min_perimeter = min(l+l+w+w, l+l+h+h, h+h+w+w)
		volume = l * w * h

		ribbon_sum += min_perimeter + volume

print(ribbon_sum)