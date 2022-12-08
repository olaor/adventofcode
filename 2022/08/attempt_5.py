# Read the input data from a file called "input.txt"
# Each line of the file contains a string representing a row of the grid
with open('input.txt') as f:
    data = f.read().strip().split('\n')

# Convert the input data to a 2D grid of integers
grid = [[int(c) for c in row] for row in data]

# Initialize the count of visible trees to 0
num_visible_trees = 0

# Iterate over the rows and columns of the grid
for i in range(len(grid)):
    for j in range(len(grid[i])):
        # Check if the current tree is visible from the left
        # by checking if all of the trees to the left of it
        # are shorter than it
        is_visible_from_left = all(grid[i][k] < grid[i][j] for k in range(j))
        
        # Check if the current tree is visible from the right
        # by checking if all of the trees to the right of it
        # are shorter than it
        is_visible_from_right = all(grid[i][k] < grid[i][j] for k in range(j+1, len(grid[i])))
        
        # Check if the current tree is visible from the top
        # by checking if all of the trees above it
        # are shorter than it
        is_visible_from_top = all(grid[k][j] < grid[i][j] for k in range(i))
        
        # Check if the current tree is visible from the bottom
        # by checking if all of the trees below it
        # are shorter than it
        is_visible_from_bottom = all(grid[k][j] < grid[i][j] for k in range(i+1, len(grid)))
        
        # If the current tree is visible from any direction,
        # increment the count of visible trees
        if is_visible_from_left or is_visible_from_right or is_visible_from_top or is_visible_from_bottom:
            num_visible_trees += 1

# Print the final count of visible trees
print(num_visible_trees)
