for a in range(1, 999):
	for b in range(1, 999):
		c = (1000 - (a + b))
		if c < 0:
			break
		if (a ** 2) + (b ** 2) == (c ** 2):
			print "Answer found!"
			print a, "+", b, "+", c, "=1000"
			print a ** 2, "+", b ** 2, "=", c ** 2
			print "Product: ", a*b*c
			quit()
