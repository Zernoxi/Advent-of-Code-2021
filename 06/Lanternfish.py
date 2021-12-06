#!/usr/bin/env python

# cSpell: disable

from os import path

def main(data, timeframe):
    i = 0
    j = 0
    k = 0
    while i < timeframe:
        while j < len(data):
            if data[j] > -1:
                data[j] -= 1
            j += 1
        while k < len(data):
            if data[k] == -1:
                data.append(NEW_LATERN)
                data[k] = LATERN
            k += 1
        i += 1
        j = 0
        k = 0
    return len(data)

if __name__ == "__main__":
    dir_path = path.dirname(__file__)
    test_path = path.join(dir_path, "test.in")
    file_path = path.join(dir_path, "data.in")

    # Inclusive of "0"
    LATERN = 6
    NEW_LATERN = 8

    # Data input is only on line 1
    with open(file_path) as data:
        dataset = list(map(int, data.readline().rstrip().split(",")))

    print("Part One:", main(dataset, 80))