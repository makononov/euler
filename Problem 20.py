def factorial(arg):
	if arg < 0:
		return None
	elif arg <= 1:
		return 1
	else:
		return arg * factorial(arg - 1)

print sum(int(digit) for digit in str(factorial(100)))
