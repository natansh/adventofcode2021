def mark_number_for_board(number, board, marker):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                marker[i][j] = True


def has_won(marker):
    # Check rows
    for i in range(5):
        if all(marker[i]):
            return True

    # Check columns
    for j in range(5):
        # Build column for j
        column = [marker[i][j] for i in range(5)]
        if all(column):
            return True


def score(board, marker):
    sum = 0
    for i in range(5):
        for j in range(5):
            if marker[i][j] == False:
                sum += board[i][j]
    return sum


def run_bingo(numbers, board_states):
    for number in numbers:
        for board, marker in board_states:
            mark_number_for_board(number, board, marker)
            if has_won(marker):
                return number * score(board, marker)


def run_bingo_last(numbers, board_states):
    last_score = 0
    has_won_before = [False] * len(board_states)
    for number in numbers:
        for (index, (board, marker)) in enumerate(board_states):
            mark_number_for_board(number, board, marker)
            if has_won(marker) and not has_won_before[index]:
                has_won_before[index] = True
                last_score = number * score(board, marker)
    return last_score


def read_numbers(file):
    return [int(num) for num in file.readline().rstrip().split(",")]


def build_board_state(lines):
    board = []
    marker = []
    for line in lines:
        board.append([int(num) for num in line.split()])
        marker.append([False] * 5)
    return (board, marker)


def read_board_states(file):
    board_states = []
    while True:
        line = file.readline()
        if not line:
            break
        lines = [file.readline().rstrip() for i in range(5)]
        board_states.append(build_board_state(lines))
    return board_states


with open("data/day4.txt") as file:
    numbers = read_numbers(file)
    board_states = read_board_states(file)

    print("Day 4 - a")
    print(run_bingo(numbers, board_states))

    print("Day 4 - b")
    print(run_bingo_last(numbers, board_states))
