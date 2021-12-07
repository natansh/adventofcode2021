from parse import parse
import numpy as np
import pandas as pd

with open("data/day7.txt") as file:
    numbers = [int(i) for i in file.readline().rstrip().split(",")]

    # Looked like it would be the median. Turned out to be the median.
    median = np.median(numbers)
    val = np.linalg.norm([n - median for n in numbers], 1)
    print(val)

    # Just went with the fastest way I can think of the problem. Find min/max, iterate.
    mi = numbers[0]
    ma = numbers[0]
    for num in numbers[1:]:    
        mi = min(num, mi)
        ma = max(num, ma)

    val = 400000000000000000000000000000
    for i in range(mi, ma + 1):
        next = sum([(abs(n - i) * (abs(n - i) + 1) / 2) for n in numbers])
        val = min(next, val)
    print(val)