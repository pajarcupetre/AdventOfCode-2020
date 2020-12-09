#!/usr/bin/python3

import sys


def process(numbers, allnumbers):
    if len(numbers) <= 25:
        return True, 0, numbers
    number_to_check = numbers[25]
    sums = set()
    for index in range(0, 24):
        for index2 in range(index + 1, 25):
            sums.add(numbers[index] + numbers[index2])
    if number_to_check in sums:
        return True, 0, numbers[1:]
    else:
        for index in range(0, len(allnumbers) - 1):
            min = allnumbers[index]
            max = allnumbers[index]
            sum = allnumbers[index]
            index2 = index + 1
            while sum + allnumbers[index2] <= number_to_check and index2 < len(allnumbers) - 1:
                sum += allnumbers[index2]
                if allnumbers[index2] < min:
                    min = allnumbers[index2]
                if allnumbers[index2] > max:
                    max = allnumbers[index2]
                if sum == number_to_check:
                    return False, min + max, numbers[1:]
                index2 += 1


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    numbers = list()
    allnumbers = list()
    for line in file:
        numbers.append((int)(line.strip()))
        allnumbers.append((int)(line.strip()))
        (isValid, sum_min_max, numbers) = process(numbers, allnumbers)
        if not isValid:
            print(line.strip(), sum_min_max)
            break
