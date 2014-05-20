from math import sqrt

def factors(num):
	factors = []
	for x in range(1, int(sqrt(num)) + 1):
		if num % x == 0:
			factors.append(x)
			if x != 1 and (num / x) not in factors:	factors.append(num / x)
	return factors
	

amicable_pairs = []

for num in range(1, 10001):
	if num not in amicable_pairs:
		sum_of_factors = sum(factors(num))
		if sum_of_factors != num and sum(factors(sum_of_factors)) == num:
			amicable_pairs.append(num)
			amicable_pairs.append(sum_of_factors)

print(sum(amicable_pairs))
