import re


forbidden_sequences = [ "ab", "cd", "pq", "xy" ]
double_letter_pattern = r"(?P<char>[A-Za-z])(?P=char)"


def has_three_vowels(string):
	vowel_count = 0
	for char in string:
		if char in "aeiou":
			vowel_count += 1
	return vowel_count >= 3


def has_double_letter(string):
	return re.search(double_letter_pattern, string) != None


def no_forbidden_sequences(string):
	for sequence in forbidden_sequences:
		if sequence in string:
			return False
	return True


total_nice_lines = 0
data = open("input", "r")
for line in data:
	if has_three_vowels(line) and has_double_letter(line) and no_forbidden_sequences(line):
		total_nice_lines += 1
data.close()
print(f"Total Nice Lines: {total_nice_lines}")