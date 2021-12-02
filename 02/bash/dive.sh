#!/usr/bin/env bash

function calculation() {
    declare -r dir="$(cd "$(dirname "${0}")" && pwd)"

    aim=0 # down increase, up decrease
    depth=0 # forward * aim increase
    position=0 # forward increase
    file="$dir/../commands.txt"

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
        echo $(( $aim * $position ))
    elif [[ $1 = "part_two" ]]; then
        echo $(( $depth * $position ))
    fi
}

function main() {
    # part_one or part_two
    arr=( "part_one" "part_two" )
    [[ -n "$1" && $# -lt 2 ]] && [[ " ${arr[*]} " =~ " $1 " ]] &&
    echo Answer: $( calculation "$1" ) ||
    read -p "Provide 'part_one' or 'part_two': " input
    check=( $input )
    while [[ -z "${check[@]}" || ${#check[@]} -gt 0 ]] &&
    ! [[ " ${arr[*]} " =~ " ${check[0]} " && ${#check[@]} -lt 2 ]]; do
        read -p "Provide 'part_one' or 'part_two': " input
        check=( $input )
    done
    echo Answer: $( calculation "$input" )
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
