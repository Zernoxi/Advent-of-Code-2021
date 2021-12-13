#!/usr/bin/env python

from os import path

def get_data(path):
    coords = {}
    with open(path) as file:
        for y, line in enumerate(file):
            for x, num in enumerate(line.rstrip()):
                coords[x, y] = int(num)
    return coords

def adj_gen(x, y):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == dy == 0:
                continue
            yield x + dx, y + dy

def main(data, part=1):
    step = 0
    flashes = 0
    while True:
        step += 1
        stack = []
        for k, _v in data.items():
            data[k] += 1
            if data[k] > 9:
                stack.append(k)
        while stack:
            point = stack.pop()
            if data[point] == 0:
                continue
            data[point] = 0
            flashes += 1
            for other in adj_gen(*point):
                if other in data and data[other] != 0:
                    data[other] += 1
                    if data[other] > 9:
                        stack.append(other)
        if part == 1 and step == 100:
            stack = []
            return flashes
        elif part == 2 and all(val == 0 for val in data.values()):
            return step

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.in")
    file_path = path.join(dir_path, "data.in")

    dataset = get_data(file_path)
    dataset_copy = dataset.copy()

    print("Part One:", main(dataset))
    print("Part Two:", main(dataset_copy, 2))