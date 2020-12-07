def binary_partition(instructions, area, lesser):
	# Base Case: no instructions remaining
	if len(instructions) == 0:
		if instructions == lesser:
			return area[0]
		else:
			return area[1]

	# Recursive Case: Multiple instructions remaining
	mid = ((area[1] - area[0]) // 2) + area[0]
	if instructions[0] == lesser:
		return binary_partition(instructions[1:], [area[0], mid], lesser)
	else:
		return binary_partition(instructions[1:], [mid, area[1]], lesser)


def row(instructions):
	return binary_partition(instructions, [0, 127], "F")

def col(instructions):
	return binary_partition(instructions, [0, 7], "L")


with open("input") as f:
	data = f.read().split("\n")

seat_ids = []

for boarding_pass in data:
	r = row(boarding_pass[:-3])
	c = col(boarding_pass[-3:])
	seat_id = (r * 8) + c
	seat_ids.append(seat_id)

seat_ids.sort()

for seat in seat_ids:
	if seat + 1 not in seat_ids and seat + 2 in seat_ids:
		print(f"Missing seat: {seat + 1}")