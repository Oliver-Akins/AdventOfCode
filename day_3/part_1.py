with open("input") as f:
	hill = f.read().split("\n")

# Index deltas
slope = [
	1, # the change in vertical height of the toboggan
	3  # the change in horizontal distance of the toboggan
]

# The starting position of the toboggan
position = [0, 0]

tree_count = 0


while position[0] < len(hill):

	# Wrap the pattern as needed
	if position[1] >= len(hill[position[0]]):
		position[1] -= len(hill[position[0]])

	# Check for trees
	if hill[position[0]][position[1]] == "#":
		tree_count += 1


	position[0] += slope[0]
	position[1] += slope[1]

print(f"Trees Hit: {tree_count}")