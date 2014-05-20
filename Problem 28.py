class SpiralRing:
  def __init__(self, start, width):
    self.start = start
    self.width = width
  
  def corners(self):
    for n in range (0, 4):
      yield (n * (self.width - 1)) + self.start

  def sum_of_corners(self):
    return sum(self.corners())

  def next_ring(self):
    new_width = self.width + 2
    new_start = self.start + (3 * (self.width - 1)) + (self.width + 1)
    return SpiralRing(new_start, new_width)

class Spiral:
  def __init__(self, size):
    self.size = size
  
  def sum_of_diagnols(self):
    diagnol_sum = 1
    ring = SpiralRing(3, 3)
    while ring.width <= self.size:
      diagnol_sum += ring.sum_of_corners()
      ring = ring.next_ring()
    return diagnol_sum

print Spiral(1001).sum_of_diagnols()