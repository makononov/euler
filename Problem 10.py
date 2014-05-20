from math import sqrt

def is_prime(number):
	prime = True
	for x in range(2, sqrt(number) + 1):
		if number % x == 0:
			prime = False
			break
	return prime

sum = 0
for x in range(2, 2000000):
	if is_prime(x):
		sum += x
		
print "The sum is: ", sum