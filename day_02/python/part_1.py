depth = 0
distance = 0

with open("../input", "r") as file:
	instructions = file.read().split("\n")

# Follow each instruction
for instruction in instructions:

	# Parse the instruction into usable data
	direction, magnitude = instruction.split(" ")
	magnitude = int(magnitude)

	# Modify the submarine coordinates as needed
	if direction == "forward": distance += magnitude
	elif direction == "up": depth -= magnitude
	else: depth += magnitude

print(f"""Distance: {distance}m
Depth: {depth}m

Puzzle Answer: {distance * depth}""")