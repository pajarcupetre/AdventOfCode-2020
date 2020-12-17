#!/usr/bin/python3

import sys
from itertools import product


def count_active(state_of_cube, dimension):
    active_energy_positions = set()
    for row in range(len(state_of_cube)):
        for col in range(len(state_of_cube[row])):
            if state_of_cube[row][col] == '#':
                position = [row, col] + [0] * (dimension - 2)
                active_energy_positions.add(tuple(position))
    for index in range(6):
        active_energy_positions = simulate(active_energy_positions, dimension)
    return len(active_energy_positions)


def simulate(energy_spots, dimension):
    next_energy_spots = set()
    neighbours_index_diff = set([i for i in product([-1, 0, 1], repeat=dimension)])
    neighbours_index_diff.remove(tuple([0] * dimension))
    potential = set()
    for energy_spot in energy_spots:
        count_active_neighbours = 0
        for diff in neighbours_index_diff:
            neighbour = list()
            for index in range(len(diff)):
                neighbour.append(energy_spot[index] + diff[index])
            if tuple(neighbour) in energy_spots:
                count_active_neighbours += 1
            else:
                potential.add(tuple(neighbour))
        if 2 <= count_active_neighbours <= 3:
            next_energy_spots.add(energy_spot)
    for non_energy_spot in potential:
        count_active_neighbours = 0
        for diff in neighbours_index_diff:
            neighbour = list()
            for index in range(len(diff)):
                neighbour.append(non_energy_spot[index] + diff[index])
            if tuple(neighbour) in energy_spots:
                count_active_neighbours += 1
        if count_active_neighbours == 3:
            next_energy_spots.add(non_energy_spot)
    return next_energy_spots


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    initial_state = list()

    for line in file:
        initial_state.append(line.strip())

    print(count_active(initial_state, 3))
    print(count_active(initial_state, 4))
