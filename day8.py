from parse import parse
import numpy as np
import pandas as pd
from itertools import permutations

# for line in file.readlines():
    #    line = line.rstrip()
    #    x1, y1, x2, y2 = parse("{:d},{:d} -> {:d},{:d}", line)

with open("data/day8.txt") as f:
    count = 0
    value = 0
    for l in f.readlines():
        words = parse("{:w} {:w} {:w} {:w} {:w} {:w} {:w} {:w} {:w} {:w} | {:w} {:w} {:w} {:w}", l.rstrip())
        input = words[:10]
        output = words[10:]
        for o in output:
            l = len(o)
            if l == 2 or l == 3 or l == 4 or l == 7:
                count += 1
    
        input = [''.join(sorted(list(word))) for word in input]
        output = [''.join(sorted(list(word))) for word in output]
        zero = [0, 1, 2, 4, 5, 6]
        one = [2, 5]
        two = [0, 2, 3, 4, 6]
        three = [0, 2, 3, 5, 6]
        four = [1, 2, 3, 5]
        five = [0, 1, 3, 5, 6]
        six = [0, 1, 3, 4, 5, 6]
        seven = [0, 2, 5]
        eight = [0, 1, 2, 3, 4, 5, 6]
        nine = [0, 1, 2, 3, 5, 6]
        numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

        for p in permutations('abcdefg'):
            valid = True
            for num in numbers:
                chars = []
                for segment in num:
                    chars.append(p[segment])
                if "".join(sorted(chars)) not in input:
                    valid = False
            if valid == True:                       
                digits = []
                for num in numbers:
                    chars = []
                    for segment in num:
                        chars.append(p[segment])
                    digits.append("".join(sorted(chars)))
                print(digits)
                od = []
                for o in output:
                    for i, d in enumerate(digits):
                        if o == d:
                            od.append(i)
                value += int("".join([str(d) for d in od]))       

    print(count)
    print(value)

    