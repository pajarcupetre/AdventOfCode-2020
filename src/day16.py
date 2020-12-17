#!/usr/bin/python3

import sys


def sum_invalid_tickets_fields(inputs):
    intervals = list()
    index = 0
    while index < len(inputs):
        if len(inputs[index]) != 0:
            intervals_on_rule = inputs[index].split(': ')[1].split(' or ')
            first_interval = intervals_on_rule[0].split('-')
            second_interval = intervals_on_rule[1].split('-')
            intervals.append((int(first_interval[0]), int(first_interval[1])))
            intervals.append((int(second_interval[0]), int(second_interval[1])))
        else:
            break
        index += 1
    index += 5
    sum = 0
    while index < len(inputs):
        fields = inputs[index].split(',')
        for field in fields:
            field = int(field)
            good_field = False
            for (start, end) in intervals:
                if start <= field <= end:
                    good_field = True
                    break
            if not good_field:
                sum += field
        index += 1
    return sum


def multiple_departure_on_my_ticket(inputs):
    intervals = dict()
    index = 0
    while index < len(inputs):
        if len(inputs[index]) != 0:
            rule_field = inputs[index].split(': ')[0]
            intervals_on_rule = inputs[index].split(': ')[1].split(' or ')
            first_interval = intervals_on_rule[0].split('-')
            second_interval = intervals_on_rule[1].split('-')
            first = (int(first_interval[0]), int(first_interval[1]))
            second = (int(second_interval[0]), int(second_interval[1]))
            intervals[rule_field] = (first, second)
        else:
            break
        index += 1
    index += 2
    my_ticket = inputs[index].split(',')
    rule_field_pos = dict()
    for field_index in range(len(my_ticket)):
        field = int(my_ticket[field_index])
        good_field = False
        rule_field_pos_local = dict()
        for rule_field in intervals:
            first = intervals[rule_field][0]
            second = intervals[rule_field][1]
            if (first[0] <= field <= first[1]) or (second[0] <= field <= second[1]):
                if rule_field not in rule_field_pos_local:
                    rule_field_pos_local[rule_field] = {field_index}
                else:
                    rule_field_pos_local[rule_field].add(field_index)
                good_field = True
        for rule_field in rule_field_pos_local:
            if rule_field in rule_field_pos:
                rule_field_pos[rule_field] = rule_field_pos[rule_field].union(rule_field_pos_local[rule_field])
            else:
                rule_field_pos[rule_field] = rule_field_pos_local[rule_field]

    index += 3
    product = 1

    while index < len(inputs):
        fields = inputs[index].split(',')
        rule_field_pos_per_ticket = dict()
        good_ticket = True
        for field_index in range(len(fields)):
            field = int(fields[field_index])
            good_field = False
            rule_field_pos_local = dict()
            for rule_field in intervals:
                first = intervals[rule_field][0]
                second = intervals[rule_field][1]
                if (first[0] <= field <= first[1]) or (second[0] <= field <= second[1]):
                    if rule_field not in rule_field_pos_local:
                        rule_field_pos_local[rule_field] = {field_index}
                    else:
                        rule_field_pos_local[rule_field].add(field_index)
                    good_field = True
            if good_field:
                for rule_field in rule_field_pos_local:
                    if rule_field in rule_field_pos_per_ticket:
                        rule_field_pos_per_ticket[rule_field] = rule_field_pos_per_ticket[rule_field].union(
                            rule_field_pos_local[rule_field])
                    else:
                        rule_field_pos_per_ticket[rule_field] = rule_field_pos_local[rule_field]
            else:
                good_ticket = False
                break
        if good_ticket:
            for rule_field in intervals:
                if rule_field in rule_field_pos_per_ticket and rule_field in rule_field_pos:
                    rule_field_pos[rule_field] = rule_field_pos_per_ticket[rule_field].intersection(
                        rule_field_pos[rule_field])
                else:
                    rule_field_pos[rule_field] = set()
        index += 1
    rule_field_column_number = dict()
    rule_field_pos_list = list(rule_field_pos.items())
    while len(rule_field_pos_list) > 0:
        rule_field_pos_list.sort(key=lambda x: len(x[1]))
        rule_field_selected = rule_field_pos_list[0]
        rule_field_pos_list = rule_field_pos_list[1:]
        for index in range(len(rule_field_pos_list)):
            rule_field_pos_list[index][1].remove(list(rule_field_selected[1])[0])
        rule_field_column_number[rule_field_selected[0]] = (list(rule_field_selected[1]))[0]

    for rule in rule_field_column_number:
        if rule.startswith('departure'):
            field = int(my_ticket[rule_field_column_number[rule]])
            product *= field
    return product


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    input_strings = list()

    for line in file:
        input_strings.append(line.strip())

    print(sum_invalid_tickets_fields(input_strings))
    print("final_product:", multiple_departure_on_my_ticket(input_strings))
