#!/usr/bin/bash

declare -i INDEX=0

WIN_INC=0
MODDED_ARR=()
FILE=".\depth.txt"

mapfile -t ARR <  <(tr -d '\r' < "$FILE") 

# Groups of three in array
for i in ${!ARR[@]}; do
    if [[ "${ARR[$(( ${i}+2 ))]}" == "" ]]; then
        break
    fi
    MODDED_ARR[${INDEX}]+=${ARR[${i}]}$'\n'${ARR[$(( ${i}+1 ))]}$'\n'${ARR[$(( ${i}+2 ))]}$'\n'
    (( INDEX++ ))
done

# Compare current and previous array
for i in ${!MODDED_ARR[@]}; do
    # Check length of array
    readarray -t TEMP_ARR < <( IFS=$'\n'; echo "${MODDED_ARR[${i}]}" )
    unset TEMP_ARR[-1]
    if [[ "${#TEMP_ARR[@]}" -eq 3 ]]; then
        # Calculate sum of array
        if [[ ${i} -eq 0 ]]; then
            CUR=$( IFS=+; echo $((${TEMP_ARR[*]})) )
        elif [[ ${i} -gt 0 ]]; then
            PRE=${CUR}
            CUR=$( IFS=+; echo $((${TEMP_ARR[*]})) )
        fi
        if [[ PRE -lt CUR && PRE -ne 0 ]]; then
            ((WIN_INC++))
        fi
    fi
done
echo ${WIN_INC}