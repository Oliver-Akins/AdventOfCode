with open("../input", "r") as file:
	data = file.read().split("\n")


def find_value(data, bit=0, sort="max"):

	if len(data) == 1:
		return data[0]

	# keep track of each value that is associated with the bit value at the bit
	# position, this is what gets passed to the recursive case
	ones = []
	zeros = []

	# Run through all the data determining the bits needed
	for d in data:
		if d[bit] == "1": ones.append(d)
		else: zeros.append(d)

	new_bit = bit + 1

	if sort == "max":
		if len(ones) >= len(zeros):
			return find_value(ones, new_bit, sort)
		else:
			return find_value(zeros, new_bit, sort)
	else:
		if len(ones) < len(zeros):
			return find_value(ones, new_bit, sort)
		else:
			return find_value(zeros, new_bit, sort)

o2 = find_value(data)
co2 = find_value(data, sort="min")


print(f"""O2 binary: {o2}
CO2 binary: {co2}

O2 decimal: {int(o2, 2)}
CO2 decimal: {int(co2, 2)}

Life support value: {int(o2, 2) * int(co2, 2)}""")