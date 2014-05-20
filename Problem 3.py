from math import sqrt, floor

def largest_prime_factor(number):
  largest = 1
  for x in range(2, int(sqrt(number))):
    if number % x == 0:
      if largest_prime_factor(x) == 1:
        largest = x
  return largest
  
print largest_prime_factor(600851475143)
        

