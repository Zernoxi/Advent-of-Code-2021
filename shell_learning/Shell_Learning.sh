#!/usr/bin/bash

# Environment variables
# IFS = Internal field separator

# "${<variable>[*|@]}"                             = If the word is double-quoted, ${<variable>[*]} expands to a single word with the value of each array member separated by the first character of IFS, and ${<variable>[@]} expands each element of name to a separate word.
# "${}"                                            = Can be used to wrap variables if they can be empty or contain spaces (or any whitespace) or special characters (wildcards).
# "${}<regex>"                                     = Can place any character after "{}".
# "${<variable>([*|@]):<start>:<length>}"          = Specify offset and length returned characters/array.
# "${#}"                                           = Length of value.
# "${<variable>(#|%)<regex>}"                      = Prefix/suffix pattern matching - remove first match
# "${<variable>(##|%%)<regex>}"                    = Double prefix/suffix pattern matching - remove last match
# "${<variable>([*|@])(^|^^)}"                     = Single is default first character uppercase otherwise first occurence uppercase. Double default is all uppercase otherwise all occurences of character.
# "${<variable>([*|@])(,|,,)}"                     = Single is default first character lowercase otherwise first occurence lowercase. Double default is all lowercase otherwise all occurences of character.
# "${<variable>([*|@])(~~)}"                       = Swap cases of all characters.
# "${<variable>([*|@])(/|//)(#|%)<regex>/<regex>}" = Swap first "<regex>" with second "<regex>". Only first occurence if "/". Can use "#|%".
# "${<variable>:-<character>}"                     = If empty output "<characters>".
# "${<variable>:+<character>}"                     = If not empty output "<characters>".
# "${<variable>:?<character>}"                     = If empty throw error "<characters>".
# "${<variable>:=<character>}"                     = Redefine "<variable>" iwth "<characters>".
# ''                                               = For special characters.
# ~                                                = Used in conjuntion with "=", means to look to the left of "=" regex.
# !                                                = Indices rather than elements in array.
# <regex>*                                         = Glob used for wildcards.
# []                                               = Old POSIX shells.
# [[]]                                             = New POSIX shells.
# ;                                                = Similar to newline.
# ()                                               = Run list of commands in subprocess.
# $()                                              = Substitute result of variable to string.
# (())                                             = Evaluate arithmetic statement.
# $(())                                            = Express arithmetic expression.

# ECHO COMMAND
# echo Hello World!

# VARIABLES
# Uppercase by convention
# Letters, numbers, underscores

# NAME="Brad"
# echo "My name is ${NAME}."

# USER INPUT
# read -p "Enter your name: " NAME
# echo "Hello ${NAME}."

# IF/THEN/ELIF/ELSE STATEMENT
# if [ "${NAME}" == "Brad" ]
# then
#     echo "Your name is Brad"
# elif [ "${NAME}" == "Jack" ]
# then
#     echo "Your name is Jack"
# else
#     echo "Your name is not Brad or Jack"
# fi

# COMPARISON
# NUM1=3
# NUM2=5

# if [ "${NUM1}" -gt "${NUM2}" ]
# then
#     echo "${NUM1} is greater than ${NUM2}"
# else
#     echo "${NUM1} is less than ${NUM2}"
# fi

########
# val1 -eq val2 Returns true if the values are equal
# val1 -ne val2 Returns true if the values are not equal
# val1 -gt val2 Returns true if val1 is greater than val2
# val1 -ge val2 Returns true if val1 is greater than or equal to val2
# val1 -lt val2 Returns true if val1 is less than val2
# val1 -le val2 Returns true if val1 is less than or equal to val2
########

# FILE CONDITION
# FILE="test.txt"
# if [ -f "${FILE}" ]
# then
#     echo "${FILE} is a file"
# else
#     echo "${FILE} is not a file"
# fi

########
# -d file   True if the file is a directory
# -e file   True if the file exists (note that this is not particularly portable, thus -f is generally used)
# -f file   True if the provided string is a file
# -g file   True if the group id is set on a file
# -r file   True if the file is readable
# -s file   True if the file has a non-zero size
# -u    True if the user id is set on a file
# -w    True if the file is writable
# -x    True if the file is an executable
########

# CASE STATEMENT
# read -p "Are you 21 or over? [Y/n] " ANSWER
# case "${ANSWER}" in
#     [yY] | [yY][eE][sS]) # Close with ")" for "if case"
#         echo "First case";; # Close with ";;" for logic
#     [nN] | [nN][oO])
#         echo "Second case";;
#     *) # Default case
#         echo "Are you 21 or over? [Y/n] ";;
# esac

# FOR LOOP
# NAMES="Brad Kevin Alice Mark"
# for NAME in ${NAMES}
#    do
#         echo "Hello ${NAME}"
# done

# FILES=$(ls *.txt)
# NEW="new"
# for FILE in ${FILES}
#     do
#         echo "Renaming ${FILE} to new-${FILE}"
#         mv ${FILE} ${NEW}-${FILE}
# done

# WHILE LOOP
# LINE=1
# "IFS=" prevents leading/trailing whitespace from being trimmed
# "-r" prevents backslash escapes from being interpreted
# "|| [[ -n "$line" ]]" prevents the last line from being ignored if it doesn't end with a '\n' (since 'read' returns a non-zero exit code when it encounters EOF)
# while IFS= read -r CURRENT_LINE || [[ -n "$CURRENT_LINE" ]]
    # do
        # echo "${LINE}: ${CURRENT_LINE}"
        # ((LINE++)) # Arithmetic statement
# done < ".\new-test.txt"

# FUNCTION
# function sayHello() {
#     echo "Hello World"
# }

# sayHello

# function greet() {
#     echo "Hello, I am ${1} and I am ${2}"
# }

# greet "Brad" "35"

# ITEM CREATION
# mkdir hello
# touch ".\hello\world.txt"
# echo "Hello World" > ".\hello\world.txt"
# echo "Created hello\world.txt"