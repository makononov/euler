from math import sqrt, floor

def triangle(num):
	return sum(range(0, num))

def factors(num):
	ret = []
	for x in range(1, int(sqrt(num)) + 1):
		if num % x == 0:
			ret.append(x)
			ret.append(num / x)
	return ret

a = 1
num = 0
num_factors = 0
while num_factors <= 500:
	num += a
	a += 1
	num_factors = len(factors(num))
	print '%i has %i factors.' % (num, num_factors)