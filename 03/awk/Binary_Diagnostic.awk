#!/usr/bin/env -S awk -f

function calculate(x, y) {
    
}

BEGIN {
    FS = "";
    # OFS = " ";
    # arg = ARGV[1];
    # ARGV[1] = ENVIRON["PWD"]"/test.txt";
}

{
    split($0, bits_arr);
    for (i = 1; i <= NF; i++) {
        col_arr_ones[i] += bits_arr[i];
    }
}

END {
    for (i = 1; i <= NF; i++) {
        col_arr_zeros[i] = NR - col_arr_ones[i];
        if (col_arr_ones[i] > col_arr_zeros[i]) {
            ++gamma[i];
        } else {
            ++epsilon[i];
        }
    }
    # if (arg == "part_one") {
    #     printf "Answer: %d", aim * position;
    # } else if (arg == "part_two") {
    #     printf "Answer: %d", depth * position;
    # }
}