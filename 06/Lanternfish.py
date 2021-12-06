#!/usr/bin/env python

from os import path

def dict_check(dict, key, value=1):
    if dict.get(key, None) == None:
        dict[key] = value
    else:
        dict[key] += value

def main(data, timeframe):
    for _ in range(timeframe):
        fishs = {}
        for lifetime, nums in data.items():
            if lifetime == 0:
                dict_check(fishs, 6, nums)
                dict_check(fishs, 8, nums)
            else:
                dict_check(fishs, lifetime-1, nums)
        data = fishs
    return sum(data.values())

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.in")
    file_path = path.join(dir_path, "data.in")

    # Inclusive of "0"
    LATERN = 6
    NEW_LATERN = 8
    data_map = {}

    # Data input is only on line 1
    with open(file_path) as data:
        dataset = list(map(int, data.readline().rstrip().split(",")))
        for i in dataset:
            dict_check(data_map, i)

    print("Part One:", main(data_map, 80))
    print("Part Two:", main(data_map, 256))