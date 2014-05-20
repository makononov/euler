GRID_WIDTH = 20
GRID_HEIGHT = 20

def num_routes(x, y):
	if x == GRID_WIDTH or y == GRID_HEIGHT:
		return 1
	else:
		return num_routes(x+1, y) + num_routes(x, y+1)

print num_routes(0, 0)