increment = 20
number = 20

for x in range(20, 1, -1):
	while number % x != 0:
		number += increment
	print number, "is divisible by", x
	increment = number

print "The final answer: ", number