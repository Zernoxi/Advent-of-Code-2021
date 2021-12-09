#!/usr/bin/env python

from os import path

class Unique:
    ONE = 2
    FOUR = 4
    SEVEN = 3
    EIGHT = 7

class Occurrence:
    B = 6
    E = 4
    F = 9

def uniqueness(data, dict):
    for number in data:
        match len(number):
            case Unique.ONE:
                dict[1] += 1
            case Unique.FOUR:
                dict[4] += 1
            case Unique.SEVEN:
                dict[7] += 1
            case Unique.EIGHT:
                dict[8] += 1

def solution(data, part=1):
    uniques = {1: 0, 4: 0, 7: 0, 8: 0}
    ssd = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}

    output_num = []

    for digits, output in data:
        uniqueness(output, uniques)
        if part == 2:
            occurrences = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
            segments = {"a": "", "b": "", "c": "", "d": "", "e": "", "f": "", "g": ""}
            for letters in digits:
                if len(letters) == Unique.ONE:
                    one = "".join(sorted(letters))
                elif len(letters) == Unique.FOUR:
                    four = "".join(sorted(letters))
                elif len(letters) == Unique.SEVEN:
                    seven = "".join(sorted(letters))
                for character in letters:
                    occurrences[character] += 1
                for key, value in occurrences.items():
                    match value:
                        case Occurrence.B:
                            segments["b"] = key
                        case Occurrence.E:
                            segments["e"] = key
                        case Occurrence.F:
                            segments["f"] = key
            segments["a"] = "".join([character for character in seven if character not in one])
            segments["c"] = one.replace(segments["f"], "")
            segments["d"] = "".join([character for character in four if character not in  segments["b"] + segments["c"] + segments["f"]])
            segments["g"] = [key for key, value in occurrences.items() if value == 7 and key != segments["d"]][0]
            temp_num = []
            for letters in output:
                temp_string = ""
                for character in letters:
                    temp_string += [k for k, v in segments.items() if v == character][0]
                temp_num.append(ssd["".join(sorted(temp_string))])
            output_num.append(int("".join(map(str, temp_num))))
    if part == 1:
        return sum(uniques.values())
    else: # part == 2
        return sum(output_num)

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.in")
    file_path = path.join(dir_path, "data.in")

    dataset = []

    # Data input is only on line 1
    with open(file_path) as file:
        data = file.readlines()
        for line in data:
            digits, output = line.rstrip().split(" | ")
            dataset.append([
                tuple(digits.split()),
                tuple(output.split())
            ])

    print("Part One:", solution(dataset))
    print("Part Two:", solution(dataset, 2))