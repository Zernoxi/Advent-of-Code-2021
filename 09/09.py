#!/usr/bin/env python

from os import path

def get_data(file):
    with open(file) as data:
        dataset = [[int(str_num) for str_num in line.rstrip()] for line in data.readlines()]
    return dataset

def main(data, part=1):
    risk_level = 0
    height = len(data)
    width = len(data[0])
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for y in range(height):
        for x in range(width):
            current = data[y][x]
            lowest = True
            for i in range(4):
                dr = y + dy[i]
                dc = x + dx[i]
                if 0 <= dr < height and 0 <= dc < width and data[dr][dc] <= current:
                    lowest = False
            if lowest:
                risk_level += current + 1
    if part == 1:
        return risk_level
    else:
        sizes = []
        nodes = set()
        # Breadth first search with unique direction. Goes through the first hit of the basin, not necessarily to the lowest point.
        for y in range(height):
            for x in range(width):
                if (y, x) not in nodes and data[y][x] != 9:
                    size = 0
                    queue = []
                    queue.append((y, x))
                    while queue:
                        y, x = queue[0]
                        queue = queue[1:]
                        if (y, x) in nodes:
                            continue
                        nodes.add((y, x))
                        size += 1
                        for i in range(4):
                            dr = y + dy[i]
                            dc = x + dx[i]
                            if 0 <= dr < height and 0 <= dc < width and data[dr][dc] != 9:
                                queue.append((dr, dc))
                    sizes.append(size)
        sizes.sort()
        return sizes[-1] * sizes[-2] * sizes[-3]

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.in")
    file_path = path.join(dir_path, "data.in")

    dataset = get_data(test_path)

    print("Part One:", main(dataset))
    print("Part Two:", main(dataset, 2))