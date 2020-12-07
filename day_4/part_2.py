import re

with open("input") as f:
	data = [x.replace("\n", " ") for x in f.read().split("\n\n")]

# The fields that passports have
fields = [
	"byr",
	"iyr",
	"eyr",
	"hgt",
	"hcl",
	"ecl",
	"pid"
]

def year_validate(min, provided, max):
	return int(min) <= int(provided) <= int(max)

def size_validate(height):
	if height.endswith("cm"):
		return 150 <= int(height[:-2]) <= 193
	elif height.endswith("in"):
		return 59 <= int(height[:-2]) <= 76
	return False

def hair_validate(colour):
	return re.match(r"#[\w]{6}", str(colour)) != None

def eye_validate(colour):
	return colour in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def pid_validate(id):
	return re.match(r"^[0-9]{9}$", str(id)) != None

valid_passports = 0

# Check all the passports for valid data
for passport in data:
	valid = True

	# Check each required field
	for field in fields:

		# Ensure passport has field
		if (i := passport.find(field)) != -1:
			value = passport[i:].split(" ")[0].split(":")[1]

			if field == "byr":
				if not year_validate(1920, value, 2002):
					valid = False
					break
			elif field == "iyr":
				if not year_validate(2010, value, 2020):
					valid = False
					break
			elif field == "eyr":
				if not year_validate(2020, value, 2030):
					valid = False
					break
			elif field == "hgt":
				if not size_validate(value):
					valid = False
					break
			elif field == "hcl":
				if not hair_validate(value):
					valid = False
					break
			elif field == "ecl":
				if not eye_validate(value):
					valid = False
					break
			elif field == "pid":
				if not pid_validate(value):
					valid = False
					break
		else:
			valid = False

	if valid:
		valid_passports += 1


print(f"Valid Passports: {valid_passports}")