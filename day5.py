import regex as re

with open("data/day5.txt") as file:
    point_occ = dict()
    for line in file.readlines():
        line = line.rstrip()
        match = re.search('(\d+),(\d+) -> (\d+),(\d+)', line)
        x1, y1, x2, y2 = (int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4)))
        if x1 == x2:
            if y1 > y2:
                temp = y1
                y1 = y2
                y2 = temp
            for y in range(y1, y2 + 1):
                if (x1, y) in point_occ:
                    point_occ[(x1, y)] += 1
                else:
                    point_occ[(x1, y)] = 1
        elif y1 == y2:
            if x1 > x2:
                temp = x1
                x1 = x2
                x2 = temp
            for x in range(x1, x2 + 1):
                if (x, y1) in point_occ:
                    point_occ[(x, y1)] += 1
                else:
                    point_occ[(x, y1)] = 1    

    count = 0
    for key, value in point_occ.items():
        if value > 1:
            count += 1

    print(count)