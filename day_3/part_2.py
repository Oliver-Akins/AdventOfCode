# with open("input", "r") as data:
data = input()

unique_houses = 1
santa_coord = [0, 0]
robo_coord = [0, 0]
historic_coords = [f"0,0"]
is_real_santa = True



# Get each instruction
for direction in data:

	# Heading north
	if direction == "^":
		if is_real_santa: santa_coord[1] += 1
		else: robo_coord[1] += 1

	# Heading south
	elif direction == "v":
		if is_real_santa: santa_coord[1] -= 1
		else: robo_coord[1] -= 1

	# Heading west
	elif direction == "<":
		if is_real_santa: santa_coord[0] -= 1
		else: robo_coord[0] -= 1

	# Heading east
	elif direction == ">":
		if is_real_santa: santa_coord[0] += 1
		else: robo_coord[0] += 1

	# Unknown input
	else: raise Exception(f"InputError: Unexpected input: {direction}")


	# Get coordinate string
	if is_real_santa: coord_string = f"{santa_coord[0]},{santa_coord[1]}"
	else: f"{robo_coord[0]},{robo_coord[1]}"


	# Check if we've been here already
	if not (coord_string in historic_coords):

		# New house, keep track of it
		unique_houses += 1
		historic_coords += [coord_string]

	is_real_santa = not is_real_santa


print(f"Total Houses With At Least One Present: {unique_houses}")