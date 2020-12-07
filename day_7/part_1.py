from random import randint

target_key = "a"
values = {}


tests = [
	"123 -> x",
	"456 -> y",
	"x AND y -> d",
	"x OR y -> e",
	"x LSHIFT 2 -> f",
	"y RSHIFT 2 -> g",
	"NOT x -> h",
	"NOT y -> i"
]


def get_operation(instr):
	if len(instr) == 3: return "ASSIGNMENT"
	elif len(instr) == 4: return "INVERT"
	else: return instr[1]


def convert_values(op_type, instr):

	def to_int(key):
		"""
		Helper function to convert a single value in an instruction to an int
		"""
		try:
			return int(key)
		except ValueError:
			try:
				return values[key]
			except KeyError:
				return None

	if op_type == "INVERT":
		instr[1] = to_int(instr[1])
	elif op_type == "ASSIGNMENT":
		instr[0] = to_int(instr[0])
	else:
		instr[0] = to_int(instr[0])
		instr[2] = to_int(instr[2])
	return instr


def execute_operation(op_type, instr):
	target = instr[-1]

	if op_type == "ASSIGNMENT": values[target] = instr[0]
	elif op_type == "INVERT": values[target] = ~instr[1] + 2**16
	elif op_type == "OR": values[target] = instr[0] | instr[2]
	elif op_type == "AND": values[target] = instr[0] & instr[2]
	elif op_type == "LSHIFT": values[target] = instr[0] << instr[2]
	elif op_type == "RSHIFT": values[target] = instr[0] >> instr[2]
	else: raise Exception(f"Input Error: Invalid Operation Type: {op_type}")


def run_instruction(instr):
	instr = instr.split(" ")
	op_type = get_operation(instr)
	instr = convert_values(op_type, instr)

	# Ensure all operation parameters were found correctly
	if None in instr: return False
	execute_operation(op_type, instr)
	return True


with open("input", "r") as data:
	lines = data.readlines()
	while "a" not in values:

		random_index = randint(0, len(lines) - 1)
		success = run_instruction(lines[random_index].strip())
		if success:
			del lines[random_index]

print(f"Value of A: {values['a']}")