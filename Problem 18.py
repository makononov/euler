SEARCH_DEPTH = 3

def best_sum(line, spot, depth):
	print "Checking (%i, %i) at a depth of %i." % (line, spot, depth)
	try:
		if depth == 0:
			return pyramid[line][spot]
		else:
			return pyramid[line][spot] + max(best_sum(line+1, spot, depth-1), best_sum(line+1, spot+1, depth-1))
	except IndexError:
		return 0


test_text = """3
7 4
2 4 6
8 5 9 3"""

pyramid_text = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

pyramid = []
for line in pyramid_text.split('\n'):
	pyramid.append([int(num) for num in line.split(' ')])

print pyramid

line = 0
spot = 0
best_path = []
mysum = 0
while line < len(pyramid):
	best_path.append(spot)
	mysum += pyramid[line][spot]
	line += 1
	if best_sum(line, spot+1, SEARCH_DEPTH) > best_sum(line, spot, SEARCH_DEPTH):
		spot += 1

print mysum
print best_path