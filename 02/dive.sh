#!/usr/bin/env bash

function calculation() {
    declare -r dir="$(cd "$(dirname "${0}")" && pwd)"

    position=0 # forward increase
    depth=0 # forward * aim increase
    aim=0 # down increase, up decrease
    file="$dir/commands.txt"

    while read -a CURRENT_LINE || [ -n "${CURRENT_LINE}" ]; do
        case "${CURRENT_LINE[0]}" in
            "down")
                aim=$(( $aim + "${CURRENT_LINE[1]//[$'\015']}" ));;
            "forward")
                position=$(( $position + "${CURRENT_LINE[1]//[$'\015']}" ))
                depth=$(( $depth + $aim * "${CURRENT_LINE[1]//[$'\015']}" ));;
            "up")
                [[ $aim -ne 0 && $aim -ge "${CURRENT_LINE[1]//[$'\015']}" ]] && aim=$(( $aim - "${CURRENT_LINE[1]//[$'\015']}" ));;
            *)
                break;;
        esac
    done < $file
    if [[ $1 = "part_one" ]]; then
        echo $(( $position * $aim ))
    elif [[ $1 = "part_two" ]]; then
        echo $(( $position * $depth ))
    fi
}

function part_one() {
    echo $( calculation "part_one" )
}

function part_two() {
    echo $( calculation "part_two" )
}

# Check if there are any arguments
if [[ ! -z "$1" ]]; then
    # Check if the function exists (bash specific)
    if declare -f "$1" > /dev/null
    then
        # call arguments verbatim
        "$@"
    else
        # Show a helpful error
        echo "'$1' is not a known function name" >&2
        exit 1
    fi
fi
