#!/usr/bin/python3

import sys
import re


def is_valid(passport):
    keys_required = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for key in keys_required:
        if not (key in passport):
            return False
    return True


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def is_valid2(passport):
    year = r"^[0-9]{4}$"
    regex = re.compile(year)
    if not ('byr' in passport and regex.search(passport['byr']) and 1920 <= int(passport['byr']) <= 2002):
        return False
    if not ('iyr' in passport and regex.search(passport['iyr']) and 2010 <= int(passport['iyr']) <= 2020):
        return False
    if not ('eyr' in passport and regex.search(passport['eyr']) and 2020 <= int(passport['eyr']) <= 2030):
        return False
    if 'hgt' in passport:
        height = passport['hgt']
        if height.endswith('cm'):
            height_in_cm = int(height[:-2])
            if not (150 <= height_in_cm <= 193):
                return False
        elif height.endswith('in'):
            height_in_inch = int(height[:-2])
            if not (59 <= height_in_inch <= 76):
                return False
        else:
            return False
    else:
        return False
    color_regex = re.compile("^#[0-9a-f]{6}$")
    if not ('hcl' in passport and color_regex.search(passport['hcl'])):
        return False
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not ('ecl' in passport and passport['ecl'] in colors):
        return False
    pid_regex = re.compile("^[0-9]{9}$")
    if not ('pid' in passport and pid_regex.search(passport['pid'])):
        return False
    return True


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    passport_details = dict()
    count = 0
    for line in file:
        if len(line.strip()) == 0:
            if len(passport_details) > 0:
                if is_valid2(passport_details):
                    count += 1
                passport_details = dict()
        else:
            details = line.split(' ')
            for detail in details:
                (key, value) = detail.split(':')
                passport_details[key] = value.strip()

    if len(passport_details) > 0:
        if is_valid2(passport_details):
            count += 1
    print("valid passports:", count)
