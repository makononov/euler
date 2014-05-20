import logging
import time

class PossiblePrime(int):
  low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257]

  def is_prime(self):
    if (self > 1373653):
      raise Exception("This function only works for values under 1,373,654.")

    if self in [-1, 0, 1]:
      return False
    
    if self < 0:
      self = PossiblePrime(-self)

    # Check division by low primes
    for x in self.low_primes:
      if self != x and self % x == 0:
        logging.debug("Not prime, divisible by {0}".format(x))
        return False

    # Check if value is 2-SPRP and 3-SPRP
    if self.b_SPRP(2) and self.b_SPRP(3):
      return True 
    
    return False

    
  def b_SPRP(self, base):
    nMinus1 = d = self - 1
    s = 0

    while (d % 2 == 0):
      s += 1
      d /= 2

    a_to_the_d = pow(base, d)

    logging.debug("s: {0}".format(s))
    logging.debug("d: {0}".format(d))

    if (a_to_the_d - 1) % self == 0:
      logging.debug("Passes first congruency test.")
      return True

    for r in range (0, s):
      if (pow(a_to_the_d, pow(2, r)) + 1) % self == 0:
        logging.debug("Passes second congruency test with r={0}.".format(r))
        return True
  
    logging.debug("Fails both congruency tests. Value is composite.")
    return False 

highest = 0, 0, 0
for a in range(-1000, 1000):
  for b in range(-999, 1000, 2):
    n = 0
    while PossiblePrime(pow(n, 2) + (n * a) + b).is_prime():
      n += 1
    if (n > highest[0]):
      highest = n, a, b
      print "New highest! n={0[0]}, a={0[1]}, b={0[2]}".format(highest)

print "Highest result: n={0[0]}, a={0[1]}, b={0[2]}".format(highest)
print "Product of coefficients: {0}".format(highest[1] * highest[2])