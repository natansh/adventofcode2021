from parse import parse
import numpy as np
import pandas as pd
from itertools import permutations

# for line in file.readlines():
    #    line = line.rstrip()
    #    x1, y1, x2, y2 = parse("{:d},{:d} -> {:d},{:d}", line)

with open("data/day9.txt") as f:
    lines = f.readlines()
    data = [[int(num) for num in line.rstrip()] for line in lines]
    array = np.array(data)
    matrix = np.pad(array, ((1, 1), (1, 1)), 'constant', constant_values = (9, 9))

    risk = 0
    width = len(matrix[0])
    height = len(matrix)
    lowest_points = []
    for i in range(1, height - 1):
        for j in range(width - 1):
            lowest = True
            if (matrix[i][j] >= matrix[i-1][j]) or matrix[i][j] >= matrix[i+1][j] or matrix[i][j] >= matrix[i][j-1] or matrix[i][j] >= matrix[i][j+1]:
                lowest = False
            if lowest == True:
                lowest_points.append((i, j))
                risk += 1 + matrix[i][j]
    print("Risk:", risk)

    basin_sizes = []
    for point in lowest_points:
        queue = [point]
        visited = [point]
        while len(queue) > 0:
            i, j = queue.pop()
            for k, l in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (k, l) not in visited and matrix[i][j] < matrix[k][l] and matrix[k][l] < 9 and k > 0 and k < height and l > 0 and l < height:
                    visited.append((k, l))
                    queue.append((k, l))
        basin_sizes.append(len(visited))
    sizes = sorted(basin_sizes)
    sizes.reverse()
    print("Product:", sizes[0] * sizes[1] * sizes[2])
            
            
