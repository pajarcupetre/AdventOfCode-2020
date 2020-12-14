#!/usr/bin/python3

import sys
from functools import reduce

def compute_first_bus_and_wait(delay_time, buses_list):
    bus_to_take = -1
    wait_time = sys.maxsize
    for bus in buses_list:
        if bus != 'x':
            bus_time = int(bus)
            if delay_time % bus_time == 0:
                bus_to_take = bus_time
                wait_time = 0
            else:
                next_run = (int(delay_time / bus_time) + 1) * bus_time
                to_wait = next_run - delay_time
                if to_wait < wait_time:
                    wait_time = to_wait
                    bus_to_take = bus_time
    return bus_to_take * wait_time

def compute_earliest_consecutive_timestamp(buses_list):

    buses = dict()

    for index in range(len(buses_list)):
        bus = buses_list[index]
        if bus != 'x':
            bus_time = int(bus)
            buses[bus_time] = index

    time = 0
    step = 1
    for bus in buses:
        while (time + buses[bus]) % bus != 0:
            time += step
        step *= bus

    return time


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    commands = list()
    index = 0
    delay = 0
    buses = list()
    for line in file:
        if index == 0:
            delay = int(line.strip())
        else:
            buses = line.strip().split(',')
        index += 1
    print(compute_first_bus_and_wait(delay, buses))
    print(compute_earliest_consecutive_timestamp(buses))
