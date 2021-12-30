increasing = 0


with open("../input", "r") as file:
	data = file.read().split("\n")

	for i in range(1, len(data)):
		delta = int(data[i - 1]) - int(data[i])

		if delta < 0:
			increasing += 1

print(f"The ocean floor has increased {increasing} times")