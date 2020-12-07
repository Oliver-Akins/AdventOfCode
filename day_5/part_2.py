import re

double_letter_pattern = r"(?P<chars>[A-Za-z]{2})\w*(?P=chars)"
triple_letter_pattern = r"(?P<chars>[A-Za-z])\w(?P=chars)"


def is_nice(string):
	return (
		re.search(double_letter_pattern, string) != None
		and
		re.search(triple_letter_pattern, string) != None
	)


total_nice_lines = 0
data = open("input", "r")
for line in data:
	if is_nice(line):
		total_nice_lines += 1
data.close()
print(f"Total Nice Lines: {total_nice_lines}")