def find_shortest_distance(directions, location, visited_locations = []):
	min_location = ["", None]

	# Iterate through places we can travel to
	for direction in directions[location]:

		if direction in visited_locations:
			continue

		# find the shortest destination
		if min_location[1]:
			if directions[location][direction] < min_location[1]:
				min_location = [
					direction,
					directions[location][direction]
				]
		else:
			min_location = [
				direction,
				directions[location][direction]
			]
	return min_location



def find_shortest_route(directions, start):
	current_location = start
	distance_travelled = 0
	visited_locations = []

	while len(visited_locations) < len(directions):
		shortest_route = find_shortest_distance(directions, current_location, visited_locations)

		if not shortest_route[1]: break

		visited_locations.append(current_location)
		distance_travelled += shortest_route[1]
		current_location = shortest_route[0]
	return distance_travelled


def create_map():
	locale = {}
	with open("input", "r") as file:
		for line in file:
			data = line.strip().split()

			# Ensure city hasn't already been assigned
			if data[0] not in locale:
				locale[data[0]] = {}
			locale[data[0]][data[2]] = int(data[-1])

			# Ensure city hasn't already been assigned
			if data[2] not in locale:
				locale[data[2]] = {}
			locale[data[2]][data[0]] = int(data[-1])
	return locale


locations = create_map()
distances = []

for location in locations:
	distances.append(find_shortest_route(
		locations,
		location
	))

print(f"Shortest Route: {min(distances)}")