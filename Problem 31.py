import time

cache = {0: []}

def count_ways(value, forms):
  try:
    return cache[value]
  except KeyError:
    cache[value] = []
    for f in forms:
      if f == value:
        cache[value].append([f])

      elif f < value:
        form_ways = count_ways(value - f, forms)
        if form_ways != None:
          for i in form_ways:
            i.append(f)
            i.sort()
            if i not in cache[value]:
              cache[value].append(i)

    if len(cache[value]) == 0 and value > 0:
      return None 

    return cache[value] 

val = 200
forms = [1, 2, 5, 10, 20, 50, 100, 200]
t1 = time.time()
ways = count_ways(val, forms)
print ways
print "Found {0} ways in {1}s.".format(len(ways), time.time() - t1)