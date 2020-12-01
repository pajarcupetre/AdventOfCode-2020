#!/usr/bin/python3

import sys

def compute_report(elements, sum_to_check):
    elements_already = set()
    for elem in elements:
        elem_to_check = sum_to_check - elem
        if elem_to_check in elements_already:
            return elem_to_check * elem
        else:
            elements_already.add(elem)
    return -1

def compute_report3(elements, sum_to_check):
    sum_created = dict()
    elements = sorted(elements)
    for index in range(len(elements)):
        index_second = index + 1
        index_third = len(elements) - 1
        while index_second < index_third:
            sum_elements = elements[index] + elements[index_second] + elements[index_third]
            if sum_elements < sum_to_check:
                index_second += 1
            elif sum_elements > sum_to_check:
                index_third -= 1
            else:
                print(elements[index])
                print(elements[index_second])
                print(elements[index_third])
                return elements[index] * elements[index_second] * elements[index_third]

    return -1


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    elements = list()
    for line in file:
        elements.append(int(line))
    print(compute_report(elements, 2020))
    print(compute_report3(elements, 2020))


