def calculation(x, y):
    total = [0, 0]
    for i, bits in enumerate((x, y)):
        for bit in bits:
            total[i] = (total[i] << 1) | bit
    return total[0] * total[1]

def part_one(data):
    mod_data = zip(*data)
    gamma = [0 if sum(bits) < len(bits) // 2 else 1 for bits in mod_data]
    epsilon = (bit ^ 1 for bit in gamma)
    return calculation(gamma, epsilon)

def part_two(data):
    mod_data = [list(new_data) for new_data in list(data)]
    def helper(data, pos, bit):
        if len(data) <= 1:
            return data

        bits = [bit_col[pos] for bit_col in data]

        if bit == 1:
            common = 1 if sum(bits) > len(bits) // 2 else 0
        else: # bit == 0
            common = 1 if sum(bits) <= len(bits) // 2 else 0

        if len(data) == 2:
            common = common ^ 1

        new_data = [data_bits for data_bits in data if data_bits[pos] == common]
        return helper(new_data, pos + 1, bit)
    
    oxygen_gen = helper(mod_data, 0, 1)
    co2_scrub  = helper(mod_data, 0, 0)

    return calculation(oxygen_gen[0], co2_scrub[0])

def main(data):
    # print(part_one(data))
    print(part_two(data))
    
if __name__ == "__main__":
    FILE = "./binary.txt"
    TEST = "./test.txt"
    with open(FILE) as f:
        data = (
            map(int, bits)
            for bits in f.read().split()
            if bits != ""
        )
    main(data)