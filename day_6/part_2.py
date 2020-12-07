with open("data") as f:
	plane = f.read()


plane = plane.split("\n\n")

count = 0
for group in plane:
	group_size = len(group.split("\n"))
	group_answers = {}
	for person in group.split("\n"):
		for q in person:
			if q not in group_answers:
				group_answers[q] = 1
			else:
				group_answers[q] += 1
	count += len([1 for v in group_answers.values() if v == group_size])

print(count)