import copy

import numpy


def convert_to_binary(list_of_digits):
    list_of_str_digits = [str(digit) for digit in list_of_digits]
    return int("".join(list_of_str_digits), 2)


with open("data/day3.txt") as f:
    # The entire input forms a matrix of integers, parse it as such.
    matrix = [[int(num) for num in list(line.rstrip())] for line in f.readlines()]

    matrix_transpose = numpy.transpose(matrix)

    # `bincount` gives the occurrences of each element in the array.
    # `argmax` returns the element having the maximum occurrences.
    # `transpose` transposes a given matrix.
    max_occurrence = [numpy.bincount(row).argmax() for row in matrix_transpose]

    # There has to be a better way to do this. :-)
    max_occurrence_complement = [1 if digit == 0 else 0 for digit in max_occurrence]

    gamma = convert_to_binary(max_occurrence)
    epsilon = convert_to_binary(max_occurrence_complement)

    print("Day 3 - a")
    print(gamma * epsilon)

    # =======================

    oxy_matrix = copy.deepcopy(matrix)

    for column_index in range(len(matrix_transpose)):
        column = [row[column_index] for row in oxy_matrix]
        bincount = numpy.bincount(column)
        max_element = 1 if len(bincount) > 1 and bincount[1] >= bincount[0] else 0
        oxy_matrix = filter(lambda x: (x[column_index] == max_element), oxy_matrix)
        if len(oxy_matrix) == 1:
            break

    oxy = convert_to_binary(oxy_matrix[0])

    co2_matrix = copy.deepcopy(matrix)
    for column_index in range(len(matrix_transpose)):
        column = [row[column_index] for row in co2_matrix]
        bincount = numpy.bincount(column)
        min_element = 0 if len(bincount) <= 1 or bincount[0] <= bincount[1] else 1
        min_element = min_element if isinstance(min_element, int) else 0
        co2_matrix = filter(lambda x: (x[column_index] == min_element), co2_matrix)
        if len(co2_matrix) == 1:
            break

    co2 = convert_to_binary(co2_matrix[0])

    print("Day 3 - b")
    print(oxy * co2)
