#!/usr/bin/python3

import sys


def tree_count(row, column, area_map, right, down):
    if row >= len(area_map):
        return 0
    else:
        next_col = (column + right) % len(area_map[row])
        next_row = row + down
        if area_map[row][column] == '#':
            return 1 + tree_count(next_row, next_col, area_map, right, down)
        else:
            return tree_count(next_row, next_col, area_map, right, down)


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    area_map = list()
    for line in file:
        area_map.append(line.strip())
    first_slop = tree_count(0, 0, area_map, 1, 1)
    second_slop = tree_count(0, 0, area_map, 3, 1)
    third_slop = tree_count(0, 0, area_map, 5, 1)
    fourth_slop = tree_count(0, 0, area_map, 7, 1)
    fifth_slop = tree_count(0, 0, area_map, 1, 2)

    print("trees:", first_slop, second_slop, third_slop, fourth_slop, fifth_slop)
    print("trees multiplied:", first_slop * second_slop * third_slop * fourth_slop * fifth_slop)
