increasing = 0

with open("../input", "r") as file:

	# parse the text file into an array of integers
	data = [int(x) for x in file.read().split("\n")]

	# iterate through the data until we don't have enough data to form a group
	# of 3 values
	for i in range(0, len(data) - 3):

		# Collect the two values for the ranges for compare
		group_1 = sum(data[i : i+3])
		group_2 = sum(data[i+1 : i+4])

		# check the delta
		if group_1 - group_2 < 0:
			increasing += 1

print(f"Number of groups increasing: {increasing}")