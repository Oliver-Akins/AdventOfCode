import sys

def find_common(*args):
	i = set.intersection(*map(set, args))
	if len(i) == 1:
		return i.pop()
	return None

def determine_priority(letter):
	v = ord(letter)
	if 97 <= v <= 122:
		return v - 96
	elif 65 <= v <= 90:
		return v - 38

def run():
	if len(sys.argv) < 2:
		print("Not enough arguments")
		return
	total = 0
	with open(sys.argv[1], "r") as f:
		for line in f:
			l = line.strip()
			l2 = f.readline().strip()
			l3 = f.readline().strip()
			x = find_common(l, l2, l3)
			total += determine_priority(x)
	print(f"Sum: {total}")

if __name__ == "__main__":
	run()