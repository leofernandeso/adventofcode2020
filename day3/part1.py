import sys

def parse_input():
    path = []
    for line in sys.stdin:
        path.append(list(line.strip()))
    return path

path = parse_input()
nrows, ncols = len(path), len(path[0])
slope_i, slope_j = (1, 3)
i = 1
j = 1
tree_count = 0
while i <= nrows:

    j = j % ncols
    if path[i-1][j-1] == '#': 
        # found a tree
        tree_count += 1

    # move
    i += slope_i
    j += slope_j

print(tree_count)
    

