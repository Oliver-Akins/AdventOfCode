import re

with open("test") as file:
	rules = file.read().split("\n")


bag_colours = {}


for rule in rules:
	container, containing = rule.split(" bags contain ", 1)
	nested = containing.replace(".", "").split(", ")

	for colour in nested:

		# End iteration if no other bags can be nested internally
		if colour == "no other bags":
			break

		print(colour)
		colour = re.match(r"^[0-9]+ (?P<colour>[A-Za-z ]+) bags?$", colour).group("colour")

		# Can nest other colours inside of the bag
		if colour not in bag_colours:
			bag_colours[colour] = [container]
		else:
			if container not in bag_colours[colour]:
				bag_colours[colour].append(container)

print(bag_colours)