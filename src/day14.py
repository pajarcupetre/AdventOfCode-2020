#!/usr/bin/python3

import sys


def compute_masked(number, mask):
    number_bin = bin(number)
    if len(number_bin) - 2 < len(mask):
        number_bin = ['0'] * (len(mask) - len(number_bin) + 2) + list(number_bin)[2:]
    number_final = list()
    for index in range(len(mask)):
        if mask[index] == 'X':
            number_final.append(number_bin[index])
        else:
            number_final.append(mask[index])
    return int(''.join(number_final), 2)


def compute_masked2(number, mask):
    number_bin = bin(number)
    if len(number_bin) - 2 < len(mask):
        number_bin = ['0'] * (len(mask) - len(number_bin) + 2) + list(number_bin)[2:]
    number_finals = list()
    number_finals.append(list())
    for index in range(len(mask)):
        if mask[index] == '0':
            for index_of_solutions in range(len(number_finals)):
                number_final = number_finals[index_of_solutions]
                number_final.append(number_bin[index])
                number_finals[index_of_solutions] = number_final
        elif mask[index] == '1':
            for index_of_solutions in range(len(number_finals)):
                number_final = number_finals[index_of_solutions]
                number_final.append(mask[index])
                number_finals[index_of_solutions] = number_final
        else:
            index_of_solutions = 0
            size = len(number_finals)
            while index_of_solutions < size:
                number_final = number_finals[index_of_solutions]
                number_final_second = number_final.copy()
                number_final.append('0')
                number_final_second.append('1')
                number_finals[index_of_solutions] = number_final
                number_finals.append(number_final_second)
                index_of_solutions += 1
    return number_finals


def sum_numbers_in_mem(commands_list):
    sum = 0
    memory = dict()
    for command in commands_list:
        (command_first, command_second) = command.split(' = ')
        if command_first == 'mask':
            mask = command_second
        else:
            number = int(command_second)
            position = int(command_first.split('[')[1][:-1])
            number_masked = compute_masked(number, mask)
            memory[position] = number_masked
    for position in memory:
        sum += memory[position]

    return sum


def sum_numbers_in_mem2(commands_list):
    sum = 0
    memory = dict()
    for command in commands_list:
        (command_first, command_second) = command.split(' = ')
        if command_first == 'mask':
            mask = command_second
        else:
            number = int(command_second)
            position = int(command_first.split('[')[1][:-1])
            address_masked_list = compute_masked2(position, mask)
            address_masked = list()
            for address in address_masked_list:
                address_masked.append(int(''.join(address), 2))

            for address in address_masked:
                memory[address] = number
    for position in memory:
        sum += memory[position]

    return sum


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    commands = list()

    for line in file:
        commands.append(line.strip())

    print(sum_numbers_in_mem(commands))
    print(sum_numbers_in_mem2(commands))
