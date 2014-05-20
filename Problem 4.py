#Returns the length of an integer
def length(num):
  test = 0
  while 10 ** test <= num:
    test += 1
    
  return test


#returns the digit at a place in an integer
def digit(num, place):
  return int((num % (10 ** (place + 1))) / (10 ** place))


#Returns True if the passed integer is palindromic
def is_palindrome(num):
  l = length(num)
  for place in range(0, (l/2)):
    if digit(num, place) != digit(num, l - place - 1):
      return False
  return True


#The main body
largest = [0, 0, 0]
for a in range(999, 0, -1):
  for b in range(a, 0, -1):
    if is_palindrome(a * b):
      if a * b > largest[2]:
        largest = [a, b, a*b]

print largest
