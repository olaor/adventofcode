
# Read the input data from a file
with open('input.txt') as f:
    data = f.read().strip().split('\n')

# Convert the input data to a 2D list of integers
trees = [[int(c) for c in row] for row in data]

edges = len(trees[0]) * 2 + len(trees) * 2 - 4

# Helper function to check if a tree at a given row and column
# is visible from the outside
def is_visible(trees, row, col):
    # Get the height of the tree at the given location
    height = trees[row][col]

    # Check if there are any taller trees in the same row to the left
    for c in range(col):
        if trees[row][c] > height:
            return False

    # Check if there are any taller trees in the same row to the right
    for c in range(col + 1, len(trees[0])):
        if trees[row][c] > height:
            return False

    # Check if there are any taller trees in the same column above
    for r in range(row):
        if trees[r][col] > height:
            return False

    # Check if there are any taller trees in the same column below
    for r in range(row + 1, len(trees)):
        if trees[r][col] > height:
            return False

    # If we reach this point, the tree is visible from the outside
    return True

# Count the number of trees that are visible from the outside
count = 0
for r in range(len(trees)):
    for c in range(len(trees[0])):
        if is_visible(trees, r, c):
            count += 1

# Print the result
print(count + edges)


# Count the edges
