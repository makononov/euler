def test_fifth_power(val):
  digits = map(int, str(val)) 
  return val == sum(i**5 for i in digits)

narc_numbs = [i for i in range(2, 999999) if test_fifth_power(i)]
print narc_numbs
print sum(narc_numbs)