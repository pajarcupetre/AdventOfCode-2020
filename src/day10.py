#!/usr/bin/python3

import sys


def multiply_1diff_3diff(numbers_list):
    numbers = sorted(numbers_list)
    count1 = 0
    count3 = 0
    index = 0
    current_voltage = 0
    while index < len(numbers):
        if numbers[index] - current_voltage == 1:
            count1 += 1
        if numbers[index] - current_voltage == 3:
            count3 += 1
        current_voltage = numbers[index]
        index += 1
    count3 += 1
    return count1 * count3


def count_posibilities(numbers_list):
    numbers = sorted(numbers_list)
    posibilities = [0] * len(numbers_list)
    index = 0
    while index < len(numbers):
        if numbers[index] <= 3:
            posibilities[index] = 1
        if index - 1 >= 0 and numbers[index] - numbers[index - 1] <= 3:
            posibilities[index] += posibilities[index - 1]
        if index - 2 >= 0 and numbers[index] - numbers[index - 2] <= 3:
            posibilities[index] += posibilities[index - 2]
        if index - 3 >= 0 and numbers[index] - numbers[index - 3] <= 3:
            posibilities[index] += posibilities[index - 3]
        index += 1
    return posibilities[len(numbers) - 1]


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    numbers = list()
    for line in file:
        numbers.append((int)(line.strip()))
    print(multiply_1diff_3diff(numbers))
    print(count_posibilities(numbers))
