from math import sqrt

def is_prime(number):
	prime = True
	for x in range(2, sqrt(number) + 1):
		if number % x == 0:
			prime = False
			break
	return prime

primes = [2]
counter = 3
while len(primes) < 10001:
	if is_prime(counter):
		primes += [counter]
	counter += 1
	
print "The answer is: ", primes[len(primes) - 1]