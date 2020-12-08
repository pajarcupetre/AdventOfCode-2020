#!/usr/bin/python3

import sys


def run_instructions(intructions_list):
    accumulator = 0
    used = [False] * len(intructions_list)
    index = 0
    used[0] = True
    while True:
        (instruction, value) = intructions_list[index].split(' ')
        if instruction == 'nop':
            index += 1
            if index == len(intructions_list):
                return True, accumulator
            if used[index]:
                return False, accumulator
            used[index] = True
        elif instruction == 'acc':
            accumulator += (int)(value)
            index += 1
            if index == len(intructions_list):
                return True, accumulator
            if used[index]:
                return False, accumulator
            used[index] = True
        elif instruction == 'jmp':
            index += (int)(value)
            index = index % len(intructions_list)
            if index == 0:
                return True, accumulator
            if used[index]:
                return False, accumulator
            used[index] = True


def change_instructions(instructions):
    for index in range(len(instructions)):
        (instruction_code, value) = instructions[index].split(' ')
        if instruction_code == 'nop':
            instructions_updated = instructions.copy()
            instructions_updated[index] = 'jmp ' + value
            (finish, value) = run_instructions(instructions_updated)
            if finish:
                return value
        elif instruction_code == 'jmp':
            instructions_updated = instructions.copy()
            instructions_updated[index] = 'nop ' + value
            (finish, value) = run_instructions(instructions_updated)
            if finish:
                return value
    return -1


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    instructions = list()
    for line in file:
        instructions.append(line.strip())
    (finish, accumulator) = run_instructions(instructions)
    print("value:", accumulator)
    accumulator = change_instructions(instructions)
    print("value:", accumulator)
