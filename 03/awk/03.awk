#!/usr/bin/env -S awk -f

function bin_con(binary) {
    decimal = 0;
    for (i = 0; i < length(binary); i++) {
        if (binary[length(binary)-i] == 1) {
            decimal += 2 ^ i;
        }
    }
    return decimal;
}

BEGIN {
    FS = "";
    # OFS = " ";
}

{
    split($0, bits_arr);
    for (i = 1; i <= NF; i++) {
        col_arr_ones[i] += bits_arr[i];
    }
}

END {
    FS = " ";
    for (i = 1; i <= NF; i++) {
        col_arr_zeros[i] = NR - col_arr_ones[i];
        if (col_arr_ones[i] > col_arr_zeros[i]) {
            gamma[i] = 1;
            epsilon[i] = 0;
        } else {
            gamma[i] = 0;
            epsilon[i] = 1;
        }
    }
    print "Part One:", bin_con(gamma) * bin_con(epsilon);
    print "Part Two:", bin_con(gamma) * bin_con(epsilon);
    # if (arg == "part_one") {
    #     printf "Answer: %d", aim * position;
    # } else if (arg == "part_two") {
    #     printf "Answer: %d", depth * position;
    # }
}