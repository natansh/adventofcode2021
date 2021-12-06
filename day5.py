from parse import parse

def increment_count(a1, a2):
    if a1 == a2:
        return 0
    elif a1 < a2:
        return 1
    else:
        return -1

def overlap_point_count(point_occ):
    count = 0
    for key, value in point_occ.items():
        if value > 1:
            count += 1
    return count

with open("data/day5.txt") as file:
    point_occ_a = dict()
    point_occ_b = dict()
    for line in file.readlines():
        line = line.rstrip()
        x1, y1, x2, y2 = parse("{:d},{:d} -> {:d},{:d}", line)
        incr_x = increment_count(x1, x2)
        incr_y = increment_count(y1, y2)
        count = max(abs(y2 - y1), abs(x2 - x1))
        
        for i in range(count + 1):
            x = x1 + incr_x * i
            y = y1 + incr_y * i
            # Part A
            if incr_x == 0 or incr_y == 0:
                point_occ_a[(x, y)] = point_occ_a.get((x, y), 0) + 1
            # Part B
            point_occ_b[(x, y)] = point_occ_b.get((x, y), 0) + 1

    print("Day 5 - a")
    print(overlap_point_count(point_occ_a))
    print("Day 5 - b")
    print(overlap_point_count(point_occ_b))