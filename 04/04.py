#!/usr/bin/env python

# // cSpell:disable

from os import path

def solution(numbers, matrices, part):
    win_board = -1
    win_element = -1
    winner = 0
    num_board_wins = []

    for i in range(len(numbers)):
        for mkey, matrix in matrices.items():
            if part == 2 and mkey in num_board_wins:
                continue
            for original_transposed in (matrix, list(zip(*matrix))):
                for idx, list_line in enumerate(original_transposed):
                    for element in list_line:
                        for key, _ in element.items():
                            if key == numbers[i]:
                                list_line[idx][key] = True
                            print(list_line[idx])
                    if all([
                        match
                        for element in list_line
                        for _, match in element.items()
                    ]):
                        if part == 1:
                            win_board = matrix
                            win_element = numbers[i]
                            winner = 1
                            break
                if winner:
                    break
            if winner:
                break
        if winner:
            break
                # for ind, element in enumerate(row):
                #     for key, __ in element.items():
                #         if key == numbers[i]:
                #             row[ind][key] = True
                # if all([
                #     match
                #     for element in row
                #     for _, match in element.items()
                # ]) or all([
                #     match
                #     for element in 
                # ]):
                    # if part == 1:
                    #     win_board = matrix
                    #     win_element = numbers[i]
                    #     break
                #     else: # part == 2
                #         # if num_board_wins[0] >= len(matrices) - 1:
                #         #     win_board = matrix
                #         #     win_element = numbers[i]
                #         #     break
                #         # else:
                #         num_board_wins.append(mkey)
                #         win_element = i
                #         continue
            # for transposed_matrix in zip(*matrix):
            #     for ind, col in enumerate(transposed_matrix):
            #         for key, value  in col.items():
            #             if key == numbers[i] and value is not True:
            #                 col[ind][key] = True
            #     if all([
            #         match
            #         for col in transposed_matrix
            #         for _, match  in col.items()
            #     ]):
            #         if part == 1:
            #             win_board = matrix
            #             win_element = numbers[i]
            #             break
            #         else: # part == 2
            #             # if num_board_wins[0] >= len(matrices) - 1:
            #             #     win_board = matrix
            #             #     win_element = numbers[i]
            #             #     break
            #             # else:
            #             num_board_wins.append(mkey)
            #             win_element = i
            #             continue
    #         if win_board != -1 and win_element != -1:
    #             # if part == 1:
    #             break
    #             # elif num_board_wins[0] >= list(matrices.keys())[-1] and part == 2:
    #             #     break
    #     if win_board != -1 and win_element != -1:
    #         # if part == 1:
    #         break
    #         # elif num_board_wins[0] >= list(matrices.keys())[-1] and part == 2:
    #         #     break
    # if part == 2:
    #     win_board = matrices[num_board_wins[-1]]

    # return sum([
    #     value
    #     for row in win_board
    #     for element in row
    #     for value, match in element.items()
    #     if match is False
    # ]) * win_element


if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.txt")
    file_path = path.join(dir_path, "bingo.txt")

    numbers = []
    matrices = {}
    temp_arr = []
    board_count = 0
    start = 0

    with open(test_path) as data:
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
    solution(numbers, matrices, 1)
    # print("Solution Part One: ", )
    # print("Solution Part Two: ", solution(numbers, matrices, 2))
    