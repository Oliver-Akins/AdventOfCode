import re


def get_code_chars(string):
	return len(string)

def get_mem_chars(string):
	return len(eval(f'"{string[1:-1]}"'))

def get_encoded_size(string):
	return len(f'{re.escape(string)}') + 2


with open("input", "r") as data:
	encoded_code_sum = 0
	code_char_sum = 0
	mem_char_sum = 0
	for line in data:
		line = line.strip()
		encoded_code_sum += get_encoded_size(line)
		code_char_sum += get_code_chars(line)
		mem_char_sum += get_mem_chars(line)

	print(f"Part 1 Solution: {code_char_sum - mem_char_sum}")
	print(f"Part 2 Solution: {encoded_code_sum - code_char_sum}")