#!/usr/bin/python3

import sys


def seats_with_passengers(grid):
    changed = True
    while changed:
        changed = False
        new_grid = list()
        for grid_line in grid:
            new_grid.append(grid_line.copy())

        rows = len(grid)
        for row in range(rows):
            cols = len(grid[row])
            for col in range(cols):
                count_others = 0
                count_others += seat_occupied(grid, row, col, -1, 0)
                count_others += seat_occupied(grid, row, col, -1, -1)
                count_others += seat_occupied(grid, row, col, -1, +1)
                count_others += seat_occupied(grid, row, col, 0, -1)
                count_others += seat_occupied(grid, row, col, 0, +1)
                count_others += seat_occupied(grid, row, col, +1, 1)
                count_others += seat_occupied(grid, row, col, +1, -1)
                count_others += seat_occupied(grid, row, col, +1, 0)
                if grid[row][col] == 'L':
                    if count_others == 0:
                        new_grid[row][col] = '#'
                        changed = True
                if grid[row][col] == '#' and count_others >= 4:
                    new_grid[row][col] = 'L'
                    changed = True
        grid = new_grid
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                count += 1
    return count


def seat_occupied(grid, row, col, inc_row, inc_column):
    rows = len(grid)
    cols = len(grid[0])
    row = row + inc_row
    col = col + inc_column
    if rows > row >= 0 and 0 <= col < cols:
        if grid[row][col] == '#':
            return 1
        if grid[row][col] == 'L':
            return 0
    return 0


def first_seat_occupied(grid, row, col, inc_row, inc_column):
    rows = len(grid)
    cols = len(grid[0])
    row = row + inc_row
    col = col + inc_column
    while rows > row >= 0 and 0 <= col < cols:
        if grid[row][col] == '#':
            return 1
        if grid[row][col] == 'L':
            return 0
        row = row + inc_row
        col = col + inc_column
    return 0


def seats_with_passengers_v2(grid):
    changed = True
    while changed:
        changed = False
        new_grid = list()
        for grid_line in grid:
            new_grid.append(grid_line.copy())

        rows = len(grid)
        for row in range(rows):
            cols = len(grid[row])
            for col in range(cols):
                count_others = 0
                count_others += first_seat_occupied(grid, row, col, -1, 0)
                count_others += first_seat_occupied(grid, row, col, -1, -1)
                count_others += first_seat_occupied(grid, row, col, -1, +1)
                count_others += first_seat_occupied(grid, row, col, 0, -1)
                count_others += first_seat_occupied(grid, row, col, 0, +1)
                count_others += first_seat_occupied(grid, row, col, +1, 1)
                count_others += first_seat_occupied(grid, row, col, +1, -1)
                count_others += first_seat_occupied(grid, row, col, +1, 0)
                if grid[row][col] == 'L':
                    if count_others == 0:
                        new_grid[row][col] = '#'
                        changed = True
                if grid[row][col] == '#' and count_others >= 5:
                    new_grid[row][col] = 'L'
                    changed = True
        grid = new_grid
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                count += 1
    return count


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    grid = list()
    for line in file:
        grid.append(list(line.strip()))
    print(seats_with_passengers(grid))
    print(seats_with_passengers_v2(grid))
