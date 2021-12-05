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
        for i in range(max(x for x, _ in co_ords) + 1)
        for j in range(max(y for _, y in co_ords) + 1)
    )

def return_overlap(grid: Grid) -> int:
    return sum(
        1
        for _, overlap in grid
        if overlap >= 2
    )

def calculation(co_ords: Co_Ordinates, grid: Grid) -> Optional[Any]:
    for (x1, y1), (x2, y2) in (co_ords[i:i+2] for i in range(0, len(co_ords), 2)):
        if x1 == x2 or y1 == y2:
            for idx, node in enumerate(grid):
                if x1 == x2:
                    dy1, dy2 = sorted((y1, y2))
                    if node[0][0] == x1 and node[0][1] in range(dy1, dy2+ 1):
                        grid[idx][1] = node[1] + 1
                elif y1 == y2:
                    dx1, dx2 = sorted((x1, x2))
                    if node[0][1] == y1 and node[0][0] in range(dx1, dx2 + 1):
                        grid[idx][1] = node[1] + 1
    return grid
        
if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.txt")
    file_path = path.join(dir_path, "input.txt")

    with open(file_path) as data:
        dataset = data.readlines()

    co_ords = _parse_co_ords(dataset)
    grid = _create_grid(co_ords)
    print("Part One: ", return_overlap(calculation(co_ords, grid)))

    # Part one only concerned about horizontal and vertical lines: x1 = x2 or y1 = y2