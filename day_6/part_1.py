with open("data") as f:
	plane = f.read()


plane = plane.split("\n\n")

count = 0
for group in plane:
	group_answers = []
	for person in group.split("\n"):
		for q in person:
			if q not in group_answers:
				group_answers.append(q)
	count += len(group_answers)

print(count)