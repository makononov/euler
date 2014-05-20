from math import sqrt

def is_prime(number):
	global primes
	prime = True
	for x in primes:
		if x > sqrt(number):
			break
		if number % x == 0:
			prime = False
			break
	return prime
	
primes = [2, 3]
sum = 5
for x in range(4, 2000000):
	if is_prime(x):
		primes += [x]
		sum += x
		
print "The sum is: ", sum
