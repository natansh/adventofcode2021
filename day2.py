with open("data/day2.txt") as f:
    lines = f.readlines()

    horizontal = 0
    depth = 0
    for line in lines:
        tokens = line.split(" ")
        instruction = tokens[0]
        value = int(tokens[1])
        if instruction == "forward":
            horizontal += value
        elif instruction == "up":
            depth -= value
        else:
            depth += value

    print("Day2 - a")
    print(depth * horizontal)

    horizontal = 0
    depth = 0
    aim = 0

    for line in lines:
        tokens = line.split(" ")
        instruction = tokens[0]
        value = int(tokens[1])
        if instruction == "forward":
            horizontal += value
            depth += aim * value
        elif instruction == "up":
            aim -= value
        else:
            aim += value

    print("Day2 - b")
    print(depth * horizontal)
