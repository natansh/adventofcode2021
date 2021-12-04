# A `with` statement is a good way of opening a file. https://www.python.org/dev/peps/pep-0343/
with open("data/day1.txt") as f:
    # List comprehension makes it easy to read the lines and conver to integer.
    numbers = [int(line) for line in f.readlines()]
    # List slicing in action. The two lists are of equal size.
    pairs = zip(numbers[:-1], numbers[1:])
    # List comprehensions used with conditions.
    increasing_count = sum([1 if y - x > 0 else 0 for (x, y) in pairs])
    print("Day1 - a")
    print(increasing_count)

    # For Part 2, the approach is similar, except we need to first build 3 item sequences, then get the sum of the
    # sequence, then we need to compare these sums to see if they're increasing.
    sequences = zip(numbers[:-2], numbers[1:-1], numbers[2:])
    seq_sum = [x + y + z for (x, y, z) in sequences]
    seq_pairs = zip(seq_sum[:-1], seq_sum[1:])
    seq_increasing_count = sum([1 if y - x > 0 else 0 for (x, y) in seq_pairs])
    print("Day1 - b")
    print(seq_increasing_count)

    # Dirty, but efficient way -
    it = iter(numbers)
    curr_seq = [next(it), next(it), next(it)]
    count = 0
    x = next(it, None)
    while x is not None:
        curr_sum = sum(curr_seq)
        curr_seq.append(x)
        curr_seq.pop(0)
        next_sum = sum(curr_seq)
        if next_sum > curr_sum:
            count += 1
        x = next(it, None)
    print(count)
