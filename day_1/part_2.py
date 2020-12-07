data = input("Input Instruction set: \n")

floor_delta = 0
first_negative_instruction = None


# Run through instruction set
for index in range(len(data)):
	char = data[index]

	# Increment floor delta
	if char == "(":
		floor_delta += 1

	# Decrement floor delta and track what the first index that causes us to go
	# negative is.
	elif char == ")":
		floor_delta -= 1
		if floor_delta == -1 and not first_negative_instruction:
			first_negative_instruction = index + 1
			break

print(f"First Negative Instruction: {first_negative_instruction}")