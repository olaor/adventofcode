# Read the input
with open('input.txt') as f:
  heights = [list(map(int, line.strip())) for line in f]

# Function that determines whether a tree is visible from the left
def is_visible_from_left(row, col):
  for i in range(col):
    if heights[row][i] > heights[row][col]:
      return False
  return True

# Function that determines whether a tree is visible from the top
def is_visible_from_top(row, col):
  for i in range(row):
    if heights[i][col] > heights[row][col]:
      return False
  return True

# Count the number of visible trees
visible_trees = 0

# Check the left and top edges
for row in range(len(heights)):
  for col in range(len(heights[row])):
    if (row == 0 or col == 0) and heights[row][col] > 0:
      visible_trees += 1

# Check the interior of the grid
for row in range(1, len(heights)):
  for col in range(1, len(heights[row])):
    if is_visible_from_left(row, col) or is_visible_from_top(row, col):
      visible_trees += 1

# Print the result
print(visible_trees)
