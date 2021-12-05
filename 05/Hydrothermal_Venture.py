#!/usr/bin/env python

# // cSpell:disable

from os import path
from typing import *

Co_Ordinates = tuple[tuple[Mapping[int, str]]]
Grid = list[list[tuple[int, int], int]]
Data = list[str]

def _parse_co_ords(dataset: Data) -> Co_Ordinates:
    return tuple(
        tuple(map(int, x_y.split(",")))
        for line in dataset
        for x_y in line.rstrip().split(" -> ")
    )

def _create_grid(co_ords: Co_Ordinates) -> Grid:
    return tuple(
        [(i, j), 0]
        for i in range(max(x for x, _ in co_ords)+1)
        for j in range(max(y for _, y in co_ords)+1)
    )

def return_overlap(grid: Grid) -> int:
    return sum(
        1
        for _, overlap in grid
        if overlap >= 2
    )

def function(m, x, c):
    return m * x + c

# By default only Part one
def calculation(co_ords: Co_Ordinates, grid: Grid, part: int) -> Grid:
    for (x1, y1), (x2, y2) in (co_ords[i:i+2] for i in range(0, len(co_ords), 2)):
        for idx, node in enumerate(grid):
            x = node[0][0]
            y = node[0][1]  
            if x1 == x2:
                dy1, dy2 = sorted((y1, y2))
                if x == x1 and y in range(dy1, dy2+1):
                    grid[idx][1] = node[1] + 1
            elif y1 == y2:
                dx1, dx2 = sorted((x1, x2))
                if y == y1 and x in range(dx1, dx2+1):
                    grid[idx][1] = node[1] + 1
            elif part == 2:
                m = (y2 - y1) // (x2 - x1)
                if m == 1 or m == -1:
                    dy1, dy2 = sorted((y1, y2))
                    for dy in range(dy1, dy2+1):
                        if function(m, x, y1-m*x1) == dy and y == dy:
                            grid[idx][1] = node[1] + 1
                            break
    return grid
        
if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.txt")
    file_path = path.join(dir_path, "input.txt")

    with open(file_path) as data:
        dataset = data.readlines()

    co_ords = _parse_co_ords(dataset)
    grid = _create_grid(co_ords)
    # print("Part One: ", return_overlap(calculation(co_ords, grid, 1)))
    print("Part Two: ", return_overlap(calculation(co_ords, grid, 2)))
    # calculation(co_ords, grid, 2)

    # Part one only concerned about horizontal and vertical lines: x1 = x2 or y1 = y2
    # Part two add diagonals