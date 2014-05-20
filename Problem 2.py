sequence = [1, 2]
sum = 0
while sequence[1] < 4000000:
  if sequence[1] % 2 == 0:
    sum += sequence[1]
  
  #Find the next term in the sequence
  next_term = sequence[0] + sequence[1]
  sequence[0] = sequence[1]
  sequence[1] = next_term

print sum
