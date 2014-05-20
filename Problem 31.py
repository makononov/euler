import time
start = time.clock()

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = {0: []}

def calculate_ways(target):
	if target < min(coins):
		raise Exception("Impossible sum")

	try: 
		return ways[target]
	except KeyError:
		ways[target] = []
		candidates = [x for x in sorted(coins, reverse=True) if x <= target]
		for coin in candidates:
			if coin == target and [coin] not in ways[target]:
				ways[target].append([coin])
			else:
				for subway in calculate_ways(target - coin):
					if sorted([coin] + subway) not in ways[target]:
						ways[target].append(sorted([coin] + subway))
		# print("Found {0} ways for {1}".format(len(ways[target]), target))
		return ways[target]
		
numways = len(calculate_ways(target))
print("Found {0} ways in {1} seconds.".format(numways, (time.clock() - start) / 1000))
