#!/usr/bin/env python

from os import path

def solution(numbers, matrices):
    win_board = -1
    win_element = -1
    for i in range(len(numbers)):
        for _, matrix in matrices.items():
            for row in matrix:
                for ind, element in enumerate(row):
                    for key, __ in element.items():
                        if key == numbers[i]:
                            row[ind][key] = True
                if all([
                    match
                    for element in row
                    for _, match in element.items()
                ]):
                    win_board = matrix
                    win_element = numbers[i]
                    break
            if win_board != -1 and win_element != -1:
                break
        if win_board != -1 and win_element != -1:
            break
        else:
            if all([
                match
                for transposed_matrix in zip(*matrix)
                for col in transposed_matrix
                for _, match  in col.items()
            ]):
                win_board = matrix
                win_element = numbers[i]
                break
    return sum([
        value
        for row in win_board
        for element in row
        for value, match in element.items()
        if match is False
    ]) * win_element


if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.txt")
    file_path = path.join(dir_path, "bingo.txt")

    numbers = []
    matrices = {}
    temp_arr = []
    board_count = 0
    start = 0

    with open(file_path) as data:
        dataset = data.readlines()
    
    for index, line in enumerate(dataset):
        line = line.rstrip()
        if "," in line:
            numbers.extend(list(map(int, line.split(","))))
        else:
            if line != "":
                temp_arr.append(tuple(map(
                    lambda element: {int(element): False},
                    line.split()
                )))
            if line == "" or index == len(dataset) - 1:
                if start != 0:
                    matrices[board_count] = temp_arr
                    temp_arr = []
                    board_count += 1
                else:
                    start += 1
    print("Solution Part One: ", solution(numbers, matrices))