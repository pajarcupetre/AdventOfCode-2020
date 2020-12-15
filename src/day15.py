#!/usr/bin/python3

import sys


def check_nth(input_list, to_check):
    last_pos = dict()
    for index in range(len(input_list) - 1):
        number = input_list[index]
        last_pos[number] = index + 1
    index = len(input_list) - 1
    last_number = input_list[index]
    while index < to_check - 1:
        if last_number in last_pos:
            number = index + 1 - last_pos[last_number]
            last_pos[last_number] = index + 1
        else:
            last_pos[last_number] = index + 1
            number = 0
        last_number = number
        index += 1
    return last_number


if __name__ == '__main__':
    input_list = (16, 11, 15, 0, 1, 7)
    input_list_test = (1, 2, 3)
    print(check_nth(input_list, 2020))
    print(check_nth(input_list, 30000000))
