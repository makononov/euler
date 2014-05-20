from math import sqrt
import threading

def is_prime(number):
	prime = True
	if number < 2:
		return False
	for x in range(2, int(sqrt(number)) + 1):
		if number % x == 0:
			prime = False
			break
	return prime

class WorkerThread (threading.Thread):
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
		threading.Thread.__init__(self)
	
	def run(self):
		my_sum = 0
		for x in range(self.begin, self.end):
			if is_prime(x):
				my_sum += x
		
		global sum
		sum += my_sum
			
sum = 0
thread = []
for x in xrange(20):
	begin = x * 100000
	end = (x+1) * 100000
	thread += [WorkerThread(begin, end)]
	print "Spawning thread #", x, "with range: ", begin, "-", end
	thread[x].start()

for x in xrange(20):
	print "Waiting for Thread #", x
	thread[x].join()
	
print "**************"
print "The sum is: ", sum
