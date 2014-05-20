SEARCH_DEPTH = 16

def best_sum(line, spot, depth):
	#print "Checking (%i, %i) at a depth of %i." % (line, spot, depth)
	try:
		if depth == 0:
			return pyramid[line][spot]
		else:
			return pyramid[line][spot] + max(best_sum(line+1, spot, depth-1), best_sum(line+1, spot+1, depth-1))
	except IndexError:
		return 0


pyramid = []
f = open('triangle.txt')
try:
	for line in f:
		pyramid.append([int(num) for num in line.split(' ')])
finally:
	f.close()

#print pyramid

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