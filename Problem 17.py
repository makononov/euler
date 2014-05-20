def sizeof(num):
	if num < 20:
		if num == 0: return 0 
		if num in [1, 2, 6, 10]: return 3
		if num in [4, 5, 9]: return 4
		if num in [3, 7, 8]: return 5 
		if num in [11, 12, 20]: return 6 
		if num in [15, 16]: return 7 
		if num in [13, 14, 19, 18]: return 8 
		if num in [17]: return 9
	elif num < 100:
		if num in range(20, 40) or num in range(80, 100): return 6 + sizeof(num % 10)
		elif num in range(40, 70): return 5 + sizeof(num % 10)
		elif num in range(70, 80): return 7 + sizeof(num % 10)
	elif num < 1000:
		s = 7 + sizeof(int(num / 100))
		if num % 100 != 0:
			s += 3 + sizeof(num % 100)
		return s
	else:
		return 11

s = 0
for x in range(1, 1001):
	size = sizeof(x)
	print "Size of %i: %i" % (x, size)
	s += size
print s