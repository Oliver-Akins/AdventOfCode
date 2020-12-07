data = input("Input Instruction set: \n")


# floor_delta = 0

# for char in data:
# 	if char == "(": floor_delta += 1
# 	elif char == ")": floor_delta -= 1


# This is equivalent to commented out code above
# DONE FOR FUN, Wouldn't use in production...
print(sum([ 1 if char == "(" else -1 for char in data]))