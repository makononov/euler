import math

def remainders(denom):
  num = 1
  while True:
    num *= 10
    yield num % denom
    num %= denom


l,n = 0,0
for denom in range(2, 1000):
  rem = []
  for r in remainders(denom):
    if r in rem:
      if len(rem) > l:
        l,n = len(rem), denom
        print "New max cycle: 1/{0} - {1} places".format(n, l)
      break
    else:
      rem.append(r)