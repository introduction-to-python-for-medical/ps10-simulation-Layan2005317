import numpy as np
import matplotlib.pyplot as plt

# Example grid dimensions and initialization
grid_size = 30
grid = np.random.choice([0, 1, 2], size=(grid_size, grid_size), p=[0.6, 0.3, 0.1])  # 0: empty, 1: orange, 2: red

# Define states for clarity
EMPTY = 0
ORANGE = 1
RED = 2

# Function to update the grid
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

# Run the simulation for multiple steps
steps = 10
for _ in range(steps):
    grid = spread_fire(grid)

# Visualize the grid
plt.imshow(grid, cmap="Oranges")
plt.show()

if 0 <= x < grid.shape[0] and 0 <= y < grid.shape[1]:



