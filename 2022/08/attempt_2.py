
with open('input.txt') as f:
    data = f.read().strip().split('\n')

# Convert the input data to a 2D list of integers
trees = [[int(c) for c in row] for row in data]
grid = trees

# initialize the count of visible trees to the number of trees on the edge
# since those are all visible by definition
visible_trees = 0

# iterate over the rows
for row in grid:
    # find the maximum value in the row
    max_value = max(row)
    # increment the count of visible trees by the number of times
    # the maximum value appears in the row
    visible_trees += row.count(max_value)

# iterate over the columns
for col in range(len(grid[0])):
    # initialize the maximum value in the column to 0
    max_value = 0
    # iterate over the rows
    for row in range(len(grid)):
        # find the maximum value in the column
        max_value = max(max_value, grid[row][col])
    # increment the count of visible trees by the number of times
    # the maximum value appears in the column
    visible_trees += sum(row[col] == max_value for row in grid)

# print the number of visible trees
print(visible_trees)
