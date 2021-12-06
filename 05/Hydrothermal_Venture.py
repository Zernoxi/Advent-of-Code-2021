#!/usr/bin/env python

# // cSpell:disable

from os import path

def solution(data, part):
    count = {}
    answer = 0

    for line in data:
        start, end = line.rstrip().split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        if x1 == x2 or y1 == y2:
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if (x, y) not in count:
                        count[(x, y)] = 0
                    count[(x, y)] += 1
        elif part == 2:
            dy = y2 - y1
            dx = x2 - x1
            for i in range(abs(dx)+1):
                x = x1 + (1 if dx > 0 else (-1 if dx < 0 else 0)) * i
                y = y1 + (1 if dy > 0 else (-1 if dy < 0 else 0)) * i
                if (x, y) not in count:
                    count[(x, y)] = 0
                count[(x, y)] += 1

    for overlap in count:
        if count[overlap] > 1:
            answer += 1
    return answer

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.txt")
    file_path = path.join(dir_path, "input.txt")

    with open(test_path) as data:
        dataset = data.readlines()
        
    print("Part One:", solution(dataset, 1))
    print("Part Two:", solution(dataset, 2))