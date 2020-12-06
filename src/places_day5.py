#!/usr/bin/python3

import sys


def get_id(code):
    column = code[-3:]
    row = code[:-3]
    row_value = get_value(row, 0, 127)
    column_value = get_value(column, 0, 7)
    return row_value * 8 + column_value


def get_value(code, first, last):
    if first == last:
        return first
    else:
        middle = (int)((first + last) / 2)
        if code[0] == 'F' or code[0] == 'L':
            return get_value(code[1:], first, middle)
        else:
            return get_value(code[1:], middle + 1, last)


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    max = 0
    ids = set()
    for line in file:
        id = get_id(line.strip())
        if id > max:
            max = id
        ids.add(id)

    print("Biggest id:", max)
    for id in sorted(ids):
        if not ((id + 1) in ids) and (id + 2) in ids:
            print("mine:", id+1)
            exit(0)
