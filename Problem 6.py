def sum_of_squares(r):
	sum = 0
	for x in r:
		sum += (x ** 2)
	return sum
	
def square_of_sum(r):
	sum = 0
	for x in r:
		sum += x
	return (sum ** 2)

print "The answer is: ", (square_of_sum(range(1, 101)) - sum_of_squares(range(1, 101)))