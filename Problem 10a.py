from math import sqrt
import threading
from time import sleep

def is_prime(number):
	prime = True
	for x in range(2, int(sqrt(number)) + 1):
		if number % x == 0:
			prime = False
			break
	return prime

class Spinlock:
  locked = False
  def lock(self):
    self.locked = True
  def release(self):
    self.locked = False
    
class Server:
	value = 2
	sum = 0
	def getValue(self):
		while getlock.locked:
			pass
		getlock.lock()
		ret = self.value
		self.value += 1
		getlock.release()
		return ret
		
	def AddToSum(self, val, thread):
		self.sum += val
		print val, "added by thread #", thread
	
class TestThread ( threading.Thread ):
	def __init__(self, number):
		self.thread_number = number
		threading.Thread.__init__(self)
		
	def run ( self ):
		val = server.getValue()
		while val < 100000:
			#print "Thread #", self.thread_number, "testing value", val
			if is_prime(val):
				server.AddToSum(val, self.thread_number)
			val = server.getValue()
			

getlock = Spinlock()
server = Server()
thread = []
for x in xrange(20):
	thread += [TestThread(x)]
	print "Spawning Thread #", x
	thread[x].start()

for x in xrange(20):
	print "Waiting for Thread #", x
	thread[x].join()
	
print "**************"
print "The sum is: ", server.sum
