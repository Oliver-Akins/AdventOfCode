with open("input") as file:
	data = file.read().split("\n")

import re

valid_passwords = 0


for password_data in data:

	rule, password = password_data.split(": ")
	rules = rule.split(" ")
	min_len, max_len = rules[0].split("-")

	if int(min_len) <= len(re.findall(rules[1], password)) <= int(max_len):
		valid_passwords += 1

print(valid_passwords)