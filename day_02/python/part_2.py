depth = 0
distance = 0
aim = 0

with open("../input", "r") as file:
	instructions = file.read().split("\n")

# Follow each instruction
for instruction in instructions:

	# Parse the instruction into usable data
	direction, magnitude = instruction.split(" ")
	magnitude = int(magnitude)

	# Modify the submarine coordinates as needed
	if direction == "forward":
		distance += magnitude
		depth += aim * magnitude
	elif direction == "up":
		aim -= magnitude
	else:
		aim += magnitude

print(f"""Distance: {distance}m
Depth: {depth}m
Aim: {aim}

Puzzle Answer: {distance * depth}""")