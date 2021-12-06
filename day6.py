from parse import parse
import numpy as np
import pandas as pd

with open("data/day6.txt") as file:
    numbers = [int(i) for i in file.readline().rstrip().split(",")]
    d = {}
    for num in numbers:
        d[num % 7] = d.get(num % 7, 0) + 1

    for i in range(256):
        spawn = d.get(0, 0)
        for j in range(1, 9):
            d[j - 1] = d.get(j, 0)
        d[6] += spawn
        d[8] = spawn
    
    print(sum(d.values()))

    

