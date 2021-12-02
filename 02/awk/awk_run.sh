#!/usr/bin/env bash

function main() {
    declare -r dir="$(cd "$(dirname "${0}")" && pwd)"

    file="$dir/../commands.txt"
    $file test.txt $1
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