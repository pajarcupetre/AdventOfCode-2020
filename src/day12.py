#!/usr/bin/python3

import sys
import math

def manhattan_distance(commands):
    direction = "E"
    current_index = 1
    position = (0, 0)
    directions = ['N', 'E', 'S', 'W']
    for command in commands:
        direction_to_go = command[0]
        steps_or_degree = int(command[1:])
        if direction_to_go == 'E' or (direction_to_go == 'F' and direction == 'E'):
            position = (position[0], position[1] + steps_or_degree)
        elif direction_to_go == 'W' or (direction_to_go == 'F' and direction == 'W'):
            position = (position[0], position[1] - steps_or_degree)
        elif direction_to_go == 'N' or (direction_to_go == 'F' and direction == 'N'):
            position = (position[0] - steps_or_degree, position[1])
        elif direction_to_go == 'S' or (direction_to_go == 'F' and direction == 'S'):
            position = (position[0] + steps_or_degree, position[1])
        elif direction_to_go == 'L':
            index = int(steps_or_degree / 90)
            current_index = (current_index - index) % 4
            direction = directions[current_index]
        elif direction_to_go == 'R':
            index = int(steps_or_degree / 90)
            current_index = (current_index + index) % 4
            direction = directions[current_index]
    return int(math.fabs(position[0]) + math.fabs(position[1]))

def manhattan_distance_with_waypoint(commands):
    waypoint = (-1, 10)
    position = (0, 0)
    for command in commands:
        direction_to_go = command[0]
        steps_or_degree = int(command[1:])
        if direction_to_go == 'E':
            waypoint = (waypoint[0], waypoint[1] + steps_or_degree)
        elif direction_to_go == 'W':
            waypoint = (waypoint[0], waypoint[1] - steps_or_degree)
        elif direction_to_go == 'N':
            waypoint = (waypoint[0] - steps_or_degree, waypoint[1])
        elif direction_to_go == 'S' :
            waypoint = (waypoint[0] + steps_or_degree, waypoint[1])
        elif direction_to_go == 'L':
            if steps_or_degree == 90:
                waypoint = (-1 * waypoint[1], waypoint[0])
            if steps_or_degree == 180:
                waypoint = (-1* waypoint[0], -1 * waypoint[1])
            if steps_or_degree == 270:
                waypoint = (waypoint[1], -1* waypoint[0])
        elif direction_to_go == 'R':
            if steps_or_degree == 90:
                waypoint = (waypoint[1], -1 * waypoint[0])
            if steps_or_degree == 180:
                waypoint = (-1 * waypoint[0], -1 * waypoint[1])
            if steps_or_degree == 270:
                waypoint = (-1 * waypoint[1], waypoint[0])
        elif direction_to_go == 'F':
            position = (position[0] + steps_or_degree * waypoint[0], position[1] + steps_or_degree * waypoint[1])

    return int(math.fabs(position[0]) + math.fabs(position[1]))

if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    commands = list()
    for line in file:
        commands.append(line.strip())
    print(manhattan_distance(commands))
    print(manhattan_distance_with_waypoint(commands))

