with open("../input", "r") as file:
	data = file.read().split("\n")

# Create an array that stores the number of 1's found in the corresponding bit
# position
ones_count = [0] * len(data[0])

# Run through all the data calculating the value of the bits
for diagnosis in data:
	for i in range(len(diagnosis)):
		if diagnosis[i] == "1":
			ones_count[i] += 1

# Convert the bit counts into the correct binary for the two types of data we
# need
binary = ""
inverted_binary = ""
for count in ones_count:
	if count > len(data) // 2:
		binary += "1"
		inverted_binary += "0"
	else:
		binary += "0"
		inverted_binary += "1"


print(f"""Binary Before Inversion: {binary}
Binary After Inversion: {inverted_binary}

Value of Binary: {int(binary, 2)}
Value of Inverted Binary: {int(inverted_binary, 2)}

Binary * Inverted Binary = {int(binary, 2) * int(inverted_binary, 2)}""")