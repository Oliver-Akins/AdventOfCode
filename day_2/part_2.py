with open("input") as file:
	data = file.read().split("\n")

import re

valid_passwords = 0


for password_data in data:

	rule, password = password_data.split(": ")
	rules = rule.split(" ")
	char = rules[1]
	pos1, pos2 = rules[0].split("-")

	if password[int(pos1)-1] == char and not password[int(pos2)-1] == char:
		valid_passwords += 1
	if not password[int(pos1)-1] == char and password[int(pos2)-1] == char:
		valid_passwords += 1

print(valid_passwords)