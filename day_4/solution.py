import hashlib

passkey = input("Input passkey here: ")


def find_suffix(passkey, leading_zeroes):
	hexkey = ""
	suffix = 0

	while hexkey[:leading_zeroes] != "0" * leading_zeroes:
		suffix += 1
		hashkey = hashlib.md5(f"{passkey}{suffix}".encode())
		hexkey = hashkey.hexdigest()

	return suffix


print(f"Part 1 Suffix = {find_suffix(passkey, 5)}")
print(f"Part 2 Suffix = {find_suffix(passkey, 6)}")