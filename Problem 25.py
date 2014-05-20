def fibo():
  a,b,i = 1,1,1
  while True:
    yield a, i
    a, b, i = b, a+b, i+1

for f, i in fibo():
  if f >= pow(10, 999):
    break

print "F({1}): {0}".format(f, i)