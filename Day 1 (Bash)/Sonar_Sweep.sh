#!/usr/bin/bash

function part_one() {
    line=1
    num_inc=0
    file=".\depth.txt"

    while IFS="" read -r current_line|| [ -n "${current_line}" ]; do
        if [[ ${line} -eq 1 ]] ; then
            cur_line=$( echo "${current_line}" )
            ((line++))
        elif [[ ${line} -gt 1 ]] ; then
            pre_line="${cur_line}"
            cur_line=$( echo "${current_line}" )
            ((line++))
        fi
        if [[ "${pre_line}" -lt "${cur_line}" && "${pre_line}" -ne 0 ]] ; then
            ((num_inc++))
        fi
    done < $file

    echo ${num_inc}    
}

function part_two() {
    declare -i index=0

    win_inc=0
    modded_arr=()
    file=".\depth.txt"

    mapfile -t arr <  <(tr -d '\r' < "$file") 

    # groups of three in array
    for i in ${!arr[@]}; do
        if [[ "${arr[$(( ${i}+2 ))]}" == "" ]]; then
            break
        fi
        modded_arr[${index}]+=${arr[${i}]}$'\n'${arr[$(( ${i}+1 ))]}$'\n'${arr[$(( ${i}+2 ))]}$'\n'
        (( index++ ))
    done

    # compare current and previous array
    for i in ${!modded_arr[@]}; do
        # check length of array
        readarray -t temp_arr < <( IFS=$'\n'; echo "${modded_arr[${i}]}" )
        unset temp_arr[-1]
        if [[ "${#temp_arr[@]}" -eq 3 ]]; then
            # calculate sum of array
            if [[ ${i} -eq 0 ]]; then
                cur=$( IFS=+; echo $((${temp_arr[*]})) )
            elif [[ ${i} -gt 0 ]]; then
                pre=${cur}
                cur=$( IFS=+; echo $((${temp_arr[*]})) )
            fi
            if [[ pre -lt cur && pre -ne 0 ]]; then
                ((win_inc++))
            fi
        fi
    done

    echo ${win_inc}
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
