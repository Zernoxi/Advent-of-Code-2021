#!/usr/bin/env bash

declare -r dir="$(cd "$(dirname "${0}")" && pwd)"

file="$dir/../test.txt"
awk_file="$dir/Binary_Diagnostic.awk"
$awk_file $file