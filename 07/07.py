#!/usr/bin/env python

from os import path
from math import floor, ceil

def fuel_used(data, pos):
    return sum(abs(n - pos) * (abs(n - pos) + 1) / 2 for n in data)

def part2(data):
    mean = sum(data) / len(data)
    return min(fuel_used(data, floor(mean)), fuel_used(data, ceil(mean)))

def part1(data):
    return min([sum(abs(num-pos) for num in data) for pos in range(min(data), max(data)+1)])

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.in")
    file_path = path.join(dir_path, "data.in")

    dataset = []

    # Data input is only on line 1
    with open(file_path) as file:
        data = file.readline().rstrip().split(",")
        for num in data:
            dataset.append(int(num))
    
    dataset.sort()
    print("Part One:", part1(dataset))
    print("Part Two:", part2(dataset))