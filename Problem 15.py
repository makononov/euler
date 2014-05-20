GRID_WIDTH = 20
GRID_HEIGHT = 20

grid = {}
for i in range(0, GRID_HEIGHT + 1):
	grid[i] = {}
grid[GRID_HEIGHT][GRID_WIDTH] = 0

for y in range(GRID_HEIGHT, -1, -1):
	for x in range(GRID_WIDTH, -1, -1):
		if y == GRID_HEIGHT or x == GRID_WIDTH:
			grid[y][x] = 1
		else:
			grid[y][x] = grid[y+1][x] + grid[y][x+1]

print grid
print grid[0][0]