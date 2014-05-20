lengths = {}
lengths[1] = 1

def seq(n):
	if n%2:
		#n is odd
		return (3*n) + 1
	else:
		return n/2

def seq_length(n):
	try:
		return lengths[n]
	except KeyError:
			next = seq(n)
			lengths[next] = seq_length(next)
			return 1 + lengths[next]

max_length = 0
max_num = 0
for n in range(1, 1000000):
	length = seq_length(n)
	if length > max_length:
		max_num = n
		max_length = length

print '%i produces a chain of length %i' % (max_num, max_length)