#!/usr/bin/env python

from os import path
from collections import defaultdict

def get_data(path):
    data = defaultdict(set)
    with open(path) as file:
        dataset = [line.rstrip().split("-") for line in file.readlines()]
        for arrive, destination in dataset:
            data[arrive].add(destination)
            data[destination].add(arrive)
    return data

def main(data, part=1):
    path_stack = [(("start",), False)]
    all_paths = set()
    while path_stack:
        path, double = path_stack.pop()

        if path[-1] == "end":
            all_paths.add(path)
            continue

        for recent in data[path[-1]]:
            if part == 1:
                if not recent.islower() or recent not in path:
                    path_stack.append(((*path, recent), False))
            else:
                if recent == "start":
                    continue
                elif recent.isupper() or recent not in path:
                    path_stack.append(((*path, recent), double))
                elif not double and path.count(recent) == 1:
                    path_stack.append(((*path, recent), True))
    return len(all_paths)

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.in")
    file_path = path.join(dir_path, "data.in")

    dataset = get_data(test_path)

    print(f"Part One: {main(dataset)}")
    print(f"Part Two: {main(dataset, 2)}")