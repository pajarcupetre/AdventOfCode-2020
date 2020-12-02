#!/usr/bin/python3

import sys


def split_password(line):
    (logic, char, password) = line.split(' ')
    logic_min = int(logic.split('-')[0])
    logic_max = int(logic.split('-')[1])
    char = char[:-1]
    return [(logic_min, logic_max), char, password]


def check_valid(logic, char, password):
    count_char_freq = 0
    for character in password:
        if character == char:
            count_char_freq += 1
    if logic[0] <= count_char_freq <= logic[1]:
        return True
    else:
        return False


def check_valid_only_one(logic, char, password):
    first_to_check = logic[0] - 1
    second_to_check = logic[1] - 1
    valid_count = 0
    if password[first_to_check] == char:
        valid_count += 1
    if password[second_to_check] == char:
        valid_count += 1
    if valid_count == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    valid = 0
    valid2 = 0
    for line in file:
        (logic, char, password) = split_password(line)
        if check_valid(logic, char, password):
            valid += 1
        if check_valid_only_one(logic, char, password):
            valid2 += 1
    print(valid)
    print(valid2)
