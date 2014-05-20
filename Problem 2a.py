def fibonacci(max):
  terms = 1, 1
  while terms[0] <= max: 
    yield terms[0]
    terms = terms[1], sum(terms)

print sum(x for x in fibonacci(4000000) if not x % 2) 