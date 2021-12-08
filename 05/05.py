#!/usr/bin/env python

# // cSpell:disable

from os import path

def draw_line(x1, y1, x2, y2, count):
    length = max(abs(x1 - x2)+1, abs(y1 - y2)+1)
    sign = lambda x: x and (-1 if x < 0 else 1)

    for i in range(length):
        x = x1 + sign(x2-x1) * i
        y = y1 + sign(y2-y1) * i
        if (x, y) not in count:
            count[(x, y)] = 0
        count[(x, y)] += 1

def solution(data, part=1):
    count = {}
    answer = 0

    for start, end  in data:
        x1, y1 = start
        x2, y2 = end
        if x1 == x2 or y1 == y2:
            draw_line(x1, y1, x2, y2, count)
        elif part == 2:
            draw_line(x1, y1, x2, y2, count)

    for overlap in count:
        if count[overlap] > 1:
            answer += 1
    return answer

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.txt")
    file_path = path.join(dir_path, "input.txt")

    dataset = []

    with open(file_path) as data:
        datalines = data.readlines()
        for line in datalines:
            start, end = line.rstrip().split(" -> ")
            dataset.append([
                list(map(int, start.split(","))),
                list(map(int, end.split(",")))
            ])

    print("Part One:", solution(dataset))
    print("Part Two:", solution(dataset, 2))