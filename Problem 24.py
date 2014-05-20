from itertools import permutations

number = "0123456789"
print "The 1,000,000th permutation is: {0}".format(list(permutations(number))[999999])