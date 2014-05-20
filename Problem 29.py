values = set() 

for a in range(2, 101):
  for b in range(2, 101):  
    val = pow(a, b)
    if val not in values:
      values.add(val)

print len(values)