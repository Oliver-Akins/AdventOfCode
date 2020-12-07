# with open("input", "r") as data:
data = input()

unique_houses = 1
current_coord = [0, 0]
historic_coords = [f"{current_coord[0]},{current_coord[1]}"]



# Get each instruction
for direction in data:

	# Heading north
	if direction == "^": current_coord[1] += 1

	# Heading south
	elif direction == "v": current_coord[1] -= 1

	# Heading west
	elif direction == "<": current_coord[0] -= 1

	# Heading east
	elif direction == ">": current_coord[0] += 1

	# Unknown input
	else: raise Exception(f"InputError: Unexpected input: {direction}")

	# Check if we've been here already
	coord_string = f"{current_coord[0]},{current_coord[1]}"
	if not (coord_string in historic_coords):

		# New house, keep track of it
		unique_houses += 1
		historic_coords += [coord_string]


print(f"Total Houses With At Least One Present: {unique_houses}")