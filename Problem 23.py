from math import sqrt
import time

abundants = []
start = time.time()
  
def factors(num):
	factors = []
	for x in range(1, int(sqrt(num)) + 1):
		if num % x == 0:
			factors.append(x)
			if x != 1 and (num / x) not in factors:	factors.append(num / x)
	return factors
  	
def isAbundant(num):
  return sum(factors(num)) > num

def sumoftwoabs(num):
  for ab in abundants:
    if (ab > num / 2):
      return False
    if (num - ab) in abundants:
      return True
  return False

def printprogress(percent):
  print "{0}% complete - {1}".format(percent, time.time() - start)

mysum = 0

for x in range(1, 28123):
  if (x % 2800 == 0):
    printprogress(x / 2800 * 10)
    
  if isAbundant(x):
    abundants.append(x)

  if not sumoftwoabs(x):
    mysum += x

print "The sum is {0}".format(mysum)
  
  
  
      