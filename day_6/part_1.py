import re

height = 1000
width = 1000

lights = []

for row in range(height):
	lights.append([])
	for _ in range(width):
		lights[row].append(False)

pattern = r"^(?P<type>toggle|turn on|turn off) (?P<coord1y>\d+),(?P<coord1x>\d+)[\sA-Za-z]+(?P<coord2y>\d+),(?P<coord2x>\d+)$"



def light_range(coord1x, coord1y, coord2x, coord2y):
	coord1x = int(coord1x)
	coord1y = int(coord1y)
	coord2x = int(coord2x)
	coord2y = int(coord2y)
	for row in range(coord1y, coord2y + 1):
		for col in range(coord1x, coord2x + 1):
			yield (row, col)



data = open("input", "r")
for instruction in data:

	# Parse instruction
	match = re.match(pattern, instruction)
	instruction_type = match.group("type")

	coordinate_generator = light_range(
		match.group("coord1x"), match.group("coord1y"),
		match.group("coord2x"), match.group("coord2y")
	)

	for coord in coordinate_generator:
		if instruction_type == "toggle":
			lights[coord[0]][coord[1]] = not lights[coord[0]][coord[1]]
		elif instruction_type == "turn on":
			lights[coord[0]][coord[1]] = True
		elif instruction_type == "turn off":
			lights[coord[0]][coord[1]] = False
		else:
			raise Exception(f"Input Error: Invalid instruction: \"{instruction_type}\"")

lights_on = 0
for row in lights:
	for light in row:
		if light:
			lights_on += 1

print(f"Total lights on: {lights_on}")