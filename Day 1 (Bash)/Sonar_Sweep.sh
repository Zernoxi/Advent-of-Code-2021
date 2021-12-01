#!/usr/bin/bash

LINE=1
NUM_INC=0

while IFS="" read -r CURRENT_LINE || [ -n "${CURRENT_LINE}" ]; do
    if [[ ${LINE} -eq 1 ]] ; then
        CUR_LINE=$( echo "${CURRENT_LINE}" )
        ((LINE++))
    elif [[ ${LINE} -gt 1 ]] ; then
        PRE_LINE="${CUR_LINE}"
        CUR_LINE=$( echo "${CURRENT_LINE}" )
        ((LINE++))
    fi
    if [[ "${PRE_LINE}" -lt "${CUR_LINE}" && "${PRE_LINE}" -ne 0 ]] ; then
        ((NUM_INC++))
    fi
done < ".\depth.txt"
echo ${NUM_INC}
