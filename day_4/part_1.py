with open("input") as f:
	data = [x.replace("\n", " ") for x in f.read().split("\n\n")]

# The fields that passports have, if True, it's required, if False, it's an
# optional field
fields = {
	"byr": True,
	"iyr": True,
	"eyr": True,
	"hgt": True,
	"hcl": True,
	"ecl": True,
	"pid": True,
	"cid": False
}

valid_passports = len(data)

for passport in data:
	for field, required in fields.items():
		if field not in passport and required:
			valid_passports -= 1
			break

print(f"Valid Passports: {valid_passports}")