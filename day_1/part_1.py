filename = input("Filename: ")

with open(filename) as file:
	data = file.read().split("\n")

for number_1 in data:
	n1 = int(number_1)
	for number_2 in data:
		n2 = int(number_2)
		if number_1 != number_2:
			if n1 + n2 == 2020:
				print(f"{n1} * {n2} = {n1 * n2}")