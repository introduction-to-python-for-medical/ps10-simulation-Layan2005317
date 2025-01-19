import random
import copy
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Simulation parameters
grid_size = 20  # Size of the grid
initial_fire_probability = 0.01 # Initial probability of a cell being on fire
time_steps = 50 # Number of time steps to simulate


def initialize_grid(size, initial_fire_probability):
    """Initializes the grid with random trees and a single fire source."""
    grid = [['.' for _ in range(size)] for _ in range(size)]
    # Randomly place trees
    for i in range(size):
        for j in range(size):
            if random.random() < initial_fire_probability:
                grid[i][j] = 'F'  # Fire
            elif random.random() > 0.2: # 80% of the grid will have trees
                grid[i][j] = 'T' # Tree
    return grid

def update_grid(grid):
    """Updates the grid based on the fire spread rules."""
    new_grid = copy.deepcopy(grid)
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 'F':
                # Spread fire to neighbors
                for x in range(max(0, i - 1), min(size, i + 2)):
                    for y in range(max(0, j - 1), min(size, j + 2)):
                        if (x != i or y != j) and grid[x][y] == 'T':
                            new_grid[x][y] = 'F'
            elif grid[i][j] == 'T': # the cell can also become empty after burning
              if random.random() < 0.05: # 5% probability of becoming empty after burning
                new_grid[i][j] = '.'
    return new_grid


def visualize_grid(grid):
    """Visualizes the grid."""
    plt.imshow([[1 if cell == 'T' else 0 if cell == '.' else 2 for cell in row] for row in grid], cmap='viridis') # cmap option can be changed
    plt.show()
    #clear_output(wait=True) # Uncomment to clear output for each step
    #plt.pause(0.1) # Uncomment for animation


# Initialize the grid
grid = initialize_grid(grid_size, initial_fire_probability)

# Simulate the fire spread
for _ in range(time_steps):
    visualize_grid(grid) # Visualize the grid in each time step
    grid = update_grid(grid)



