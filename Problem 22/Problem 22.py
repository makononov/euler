def alpha_sum(name):
	return sum((ord(letter) - 64) for letter in name)
	
names = [name.strip('"') for name in open('names.txt').readline().split(',')]
names.sort()

print sum((alpha_sum(name) * (names.index(name) + 1)) for name in names)