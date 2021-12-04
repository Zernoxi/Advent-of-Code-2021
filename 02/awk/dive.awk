#!/usr/bin/env -S awk -f

BEGIN {
    aim = 0;
    depth = 0;
    position = 0;
    arg = ARGV[1];
    ARGV[1] = ENVIRON["PWD"]"/commands.txt";
}

$1 == "down" { 
    aim += $2;
}

$1 == "forward" { 
    position += $2;
    depth += aim * $2;
}

$1 == "up" {
    if (aim != 0 && aim >= $2) {
        aim -= $2;
    }
}

END {
    if (arg == "part_one") {
        printf "Answer: %d", aim * position;
    } else if (arg == "part_two") {
        printf "Answer: %d", depth * position;
    }
}