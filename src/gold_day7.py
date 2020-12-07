#!/usr/bin/python3

import sys


def parse_rules(rules_list):
    dependency_hold_by = dict()
    for rule in rules_list:
        (color_holder, holds) = rule.split(' bags contain ')
        holds = holds[:-1]
        holds_colors = holds.split(', ')
        # 'light tomato bags contain 1 drab chartreuse bag, 1 dotted tomato bag, 3 striped red bags, 2 vibrant violet bags.'
        for color_part_bag in holds_colors:
            parsed = color_part_bag.split(' ')
            bag_color = parsed[1] + ' ' + parsed[2]
            if bag_color in dependency_hold_by:
                colors_already = dependency_hold_by[bag_color]
                colors_already.append(color_holder)
                dependency_hold_by[bag_color] = colors_already
            else:
                dependency_hold_by[bag_color] = [color_holder]
    return dependency_hold_by


def parse_rules2(rules_list):
    dependency_holds = dict()
    for rule in rules_list:
        (color_holder, holds) = rule.split(' bags contain ')
        holds = holds[:-1]
        holds_colors = holds.split(', ')
        # 'light tomato bags contain 1 drab chartreuse bag, 1 dotted tomato bag, 3 striped red bags, 2 vibrant violet bags.'
        holds_list = list()
        for color_part_bag in holds_colors:
            parsed = color_part_bag.split(' ')
            bag_color = parsed[1] + ' ' + parsed[2]
            count = parsed[0]
            if count != 'no':
                holds_list.append((bag_color, (int)(count)))
        if len(holds_list) > 0:
            dependency_holds[color_holder] = holds_list
    return dependency_holds


def count_back(dependencies, color):
    if not (color in dependencies):
        return set()
    else:
        bags = set(dependencies[color])
        for color_back in dependencies[color]:
            bags = bags.union(count_back(dependencies, color_back))
        return bags


def sum_bags(dependency, color):
    if not (color in dependency):
        return 0
    else:
        sum = 0
        for (bag_color, count) in dependency[color]:
            sum += count + count * sum_bags(dependency, bag_color)
        return sum


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    rules = list()
    for line in file:
        rules.append(line.strip())
    dependency_created = parse_rules(rules)
    print("colors that could hold shiny gold:", len(count_back(dependency_created, 'shiny gold')))
    dependency_with_numbers = parse_rules2(rules)
    print("bag with in shiny gold:", sum_bags(dependency_with_numbers, 'shiny gold'))
