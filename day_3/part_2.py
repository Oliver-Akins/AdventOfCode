with open("input") as f:
	hill = f.read().split("\n")

# Index deltas
slopes = [
	[1, 1], # right 1, down 1
	[1, 3], # right 3, down 1
	[1, 5], # right 5, down 1
	[1, 7], # right 7, down 1
	[2, 1]  # right 1, down 2
]

# The starting position of the toboggan

tree_counts = []

for slope in slopes:

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

	tree_counts.append(tree_count)

total = 1
for x in tree_counts:
	total *= x
print(tree_counts, total)