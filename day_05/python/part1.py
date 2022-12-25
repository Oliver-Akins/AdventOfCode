stacks = {}
with open("test") as f:
	for l in f:
		if l == "\n": break
		for i in range(len(l)):
			if i % 4 == 1 and l[i] != " ":
				s = i // 4
				if s not in stacks: stacks[s] = []
				stacks[s].append(l[i])
print(stacks)