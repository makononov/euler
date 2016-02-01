def digits(x):
    if x >= 100 or x < 10:
        raise Exception("Number out of range")
    return x // 10, x % 10

def canceled(x, y):
    numDigits = digits(x)
    denDigits = digits(y)
    if numDigits[0] in digits(y):
        cancelDigit = numDigits[0]
        num = numDigits[1]
    else:
        cancelDigit = numDigits[1]        
        num = numDigits[0]
    if cancelDigit == 0:
      raise ZeroDivisionError()
    den = [a for a in denDigits if a != cancelDigit][0]
    return num / den
        
    
numerator = 1
denominator = 1
for x in range(10, 100):
    for y in range(x, 100):
        numDigits = digits(x)
        if x != y and (numDigits[0] in digits(y) or numDigits[1] in digits(y)):
            try:
                if canceled(x, y) == x / y:
                    numerator *= x
                    denominator *= y
            except ZeroDivisionError:
                pass
            except IndexError:
                pass
              
print "{0} / {1}".format(numerator, denominator)
