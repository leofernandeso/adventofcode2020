import sys
from functools import reduce

def parse_input():
    path = []
    for line in sys.stdin:
        path.append(list(line.strip()))
    return path

def count_trees(path, slope):
    
    # Init
    nrows, ncols = len(path), len(path[0])
    slope_i, slope_j = slope
    i = 0
    j = 0
    tree_count = 0

    # Counting trees
    while (i < nrows):
        j = j % ncols
        if path[i][j] == '#': 
            tree_count += 1     # Found tree

        # Moving
        i += slope_i
        j += slope_j

    return tree_count

path = parse_input()
slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
counts = [count_trees(path, slope) for slope in slopes]
result = reduce(lambda x, y: x * y, counts)
print(result)

    

