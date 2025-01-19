import copy

def spread_fire(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == RED:
                # Spread to neighbouring orange cells
                for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:  # Boundary check
                        if grid[x, y] == ORANGE:
                            new_grid[x, y] = RED
    return new_grid




