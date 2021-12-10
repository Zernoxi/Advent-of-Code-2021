#!/usr/bin/env python

from os import path, stat

def get_data(file):
    dataset = []
    with open(file) as data:
        dataset = [line.rstrip() for line in data.readlines()]

    return dataset

def main(data, part=1):
    """
    Valid delimiters: (), [], {}, <>
    - Nesting of delimiters are allowed.
    - Multiple chucks within a delimiter is allowed.
    - Corrupted line is one where delimiter 'closes' with wrong pair.
    """
    uncorrupt = []
    complete_score = []
    corrupt = 0
    corrupt_score = 0
    delim = {"(": ")", "[": "]", "{": "}", "<": ">"}
    delim_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    auto_score = {")": 1, "]": 2, "}": 3, ">": 4}

    for line in data:
        queue = []
        for character in line:
            if character in delim.keys():
                queue.append(character)
            else:
                if delim[queue[-1]] == character:
                    queue.pop()
                else:
                    corrupt = 1
                    corrupt_score += delim_score[character]
                    break
        if corrupt:
            corrupt = 0
            continue
        else:
            uncorrupt.append(line)

    if part == 2:
        for newline in uncorrupt:
            stack = []
            score = 0
            for char in newline:
                if char in delim.keys():
                    stack.append(char)
                else:
                    if delim[stack[-1]] == char:
                        stack.pop()
            stack.reverse()
            for symbol in stack:
                score = score * 5
                score += auto_score[delim[symbol]]
            complete_score.append(score)
        complete_score.sort()
        return complete_score[len(complete_score) // 2]
    return corrupt_score

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.in")
    file_path = path.join(dir_path, "data.in")

    dataset = get_data(file_path)

    print("Part One:", main(dataset))
    print("Part Two:", main(dataset, 2))