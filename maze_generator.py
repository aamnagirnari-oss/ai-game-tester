import random

def generate_maze(rows=5, cols=5, obstacle_prob=0.3):
    grid = []

    for i in range(rows):
        row = []
        for j in range(cols):
            if random.random() < obstacle_prob:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)

    # ensure start & goal are free
    grid[0][0] = 0
    grid[rows-1][cols-1] = 0

    return grid