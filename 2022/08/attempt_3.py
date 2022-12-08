import sys
# Read the map from standard input
map = []
for line in sys.stdin:
    map.append([int(c) for c in line.strip()])

# Get the dimensions of the map
n_rows = len(map)
n_cols = len(map[0])

# Set up a counter for the number of visible trees
visible_trees = 0

# Check each row and column of the map
for i in range(n_rows):
    # Check each row
    max_in_row = max(map[i])
    visible_trees += map[i].count(max_in_row)

    # Check each column
    max_in_col = max([map[j][i] for j in range(n_rows)])
    visible_trees += [map[j][i] for j in range(n_rows)].count(max_in_col)

# Print the number of visible trees
print(visible_trees)
