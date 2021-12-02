#!/usr/bin/env -S awk -f

# STRUCTURE OF AN AWK PROGRAM

# pattern { action }
# Awk scans a sequence of input lines one after another searching for lines that are matched.
# Every input line is tested against each pattern in turn.
# For each matched. the { action } is executed.
# After every applicable { action } is executed, the next line is processed.
# ACtions are enclosed in braces to distinguish them from the pattern.
# Either the pattern or the action can be omitted.
# If the pattern is omitted, every line will match. (e.i. "{ print $1 }")
# If the action is omitted, every matching line will be printed. (e.i. "/regex/")

# AWK PATTERNS

# Awk patterns are basically just "if" statements to decide to execute the action.
# Decide if a match is TRUE or FALSE.
# If TRUE, execute the following action.
# If FALSE, skip the action and proceed to test the next pattern with current line.

########
# BEGIN { statements }                 = Statements are executed once before any input has been read.
# END { statements }                   = Statements are executed once after all input has been read.
# expression { statements }            = Statements are executed at each input line where the expression is true, that is, nonzero or nonnull.
# /regular expression/ { steatements } = Statements are executed at each input line that contains a string matched by regular expression.
# compound pattern { statements }      = Compound pattern combines expression with && (AND), || (OR), ! (NOT), and parentheses; statements are executed at each input line where the compound pattern is true.
# pattern_1, pattern_2 { statements }  = A range pattern matches each input line from a line matched by pattern_1 to the next line matched by pattern_2, inclusive; the statements are executed at each matching line.
########

########
# <  = Less than
# <= = Less than or equal to
# == = Equal to
# != = Not equal to
# >= = Greater than or equal to
# >  = Greater than
# ~  = Matched by
# !~ = Not matched by
########

# EXAMPLES
########
# NF < 10 # Num Fields
# NR <= 150 # Num Records
# $1 == "SomeString"
# $4 ~ /linux/ (or "linux")
# $5 !~ /awk/
# $2/$3 >= 0.5
########

# STRING-MATCHING PATTERN
########
# /regexpr/ (implies "$0 ~") = Matches when the current input line contains a substring matched by regexpr.
# expression ~ /regexpr/ = Matches if the string value of expression contains a substring matched by regexpr.
# expression !~ /regexpr/ = Matches if the string value of expression does not contain a substring matched by regexpr.
########
# Any expression may be used in place of /regexpr/ in the context of ~ and !~.

# ESCAPE SEQUENCES
########
# \b = backspace
# \f = formfeed
# \n = newline
# \r = carriage return
# \t = tab
# \ddd = octal value (ddd), where (ddd) is 1 to 3 digits between 0 and 7.
# \c = any other character c literally. (e.g. \\ for backslash, \" for ")
########

# AWK RANGE PATTERNS

# A range pattern consists of two patterns separated by a comma.
# A range pattern matches each line between an occurence of pattern 1 and the next occurrence of pattern 2 inclusive.
# If no instance of the second pattern is subsequently found, then all lines to end of the input are matched.

# AWK ACTIONS
# Executed if the pattern matches. (if there was a no pattern)
# Are much like a typical language. (such as C)
# Have access to a number of built in variables.
# Can create variables or call funcitons. (such as print)
# Parenthesis in function calls are optional.
# Can override fields or create new fields.

# EXAMPLE
########
# expressions, with constants, variables, assignments, function calls, etc.
# print expression-list
# printf(format, expression-list)
# if(expression) statement
# if(expression) statement else statement
# while(expression) steatement
# for(expression; expression; expression) steatement
# for(variable in array) steatement
# do statement while(expresssion)
# break
# continue
# next
# exit
# exit expression
# { statements }
########

# AWK EXAMPLES
########
# awk "{ print $2 }"                                                => print second columnn of every line.
# awk "{ print }"                                                   => print every line. (with default argument, which is $0)
# awk "{ print $0 }"                                                => print every line.
# awk "{ print $1, $3 }"                                            => print first and third columns. (columns are separated by IFS), (printed out by OFS)
# awk "{ print $1, $2 * $3 }"                                       => column math.
# awk "$3 == 10"                                                    => print whole line if third column is literal 10.
# awk "{ print NF }"                                                => print number of fields. (columns)
# awk "{ print NR, $0 }"                                            => print number of lines read. (basically line numbers)
# awk "{ print $1 "makes" $3 "per hour" }"                          => print number of fields. (columns)
# awk "{ printf("%s makes $%.2f per hour\n", $1, $3) }"             => print number of fields. (columns)
# awk "{ print $1 "makes" $3 "per hour" }" | sort -nk 3             => sort the output by $ per hour.
# awk "{ printf("%s makes $%.2f per hour\n", $1, $3) }" | uniq -f 2 => print number of fields. (columns)
########

# BUILT-IN VARIABLES
########
# ARGC          = number of command-line arguments.
# ARGV          = array of command-line arguments.
# FILENAME      = name of current input file.
# FNR           = record number in current file.
# FS " "        = controls the input field separator.
# NF            = number of fields in current record.
# NR            = number of records read so far.
# OFMT "%.6g"   = output format for numbers.
# OFS " "       = output field separator.
# ORS "\n"      = output record separator.
# RLENGTH       = length of string matched by match function.
# RS "\n"       = controls the input record separator.
# RSTART        = start of string matched by match function.
# SUBSEP "\034" = subscript separator.
########

# BUILT-IN MATH FUNCTIONS
########
# atan2(y,x) = arctangent of y/x in the range -π to π
# cos(x)     = cosine of x, with x in in radians.
# exp(x)     = exponential function of x, eˣ
# int(x)     = integer part of x; truncated towards 0 when x > 0.
# log(x)     = natural logarithm of x. (ln(x))
# rand()     = random number r, where 0 <= r < 1.
# sin(x)     = sine of x, with x in radians.
# sqrt(x)    = square root of x.
# srand(x)   = x is new seed for rand().
########

# BUILT-IN STRING FUNCTIONS
########
# gsub(r,s) = substitute s for r globally in $0, return number of substitutions made.
# gsub(r,s,t) = substitute s for r globally in string t, return number of substitutions made.
# index(s,t) = return firts position of string t in s, or 0 if t is not present.
# length(s) = return number fo characters in s.
# match(s,r) = test whether s contains a substring matched by r; return index or 0; sets RSTART and RLENGTH.
# split(s,a) = split s into array a on FS, return number of fields.
# split(s,a,fs) = split s into array a on field separator fs, return number of fields.
# sprintf(fmt,expr-list) = return expr-list formatted according to format string fmt.
# sub(r,s) = substitute s for the leftmost longest substring of $0 matched by r; return number of substitutions made.
# sub(r,s,t) = substitute s for the leftmost longest substring of t matched by r; return number of substitutions made.
# substr(s,p) = return suffix of s starting at position p.
# substr(s,p,s) = return suffix of s of length n starting at position p.
########

# EXAMPLES
########
# { gsub(/USA/, "United States"); print } => implicit argument is $0.
# x = sprintf("%10s, %6d", $1, $2)        => store into x.
# { gsub(/ana/, "anda", "banana") }       => explicit argument. operate on "banana".
# print $2 $3                             => concatenate fields 2 and 3.
########

# TYPES
# Types will automatically coereced when needed.
########
# Strings => "Strings literal"
# Numbers => (+1 1. 0 1e0 -. 1e+ 10E-1 001)
########

# CONTROL FLOW

# Most standard control flow is supported.
# Syntax is like C.

# OUTPUT STATEMENT
########
# close(filename), close(command) = break connection between print and filename or command.
# system(command)                 = execute command; value is status return of command.
########

# DEEPER UNDERSTANDING

# ARRAY

# One dimensional.
# For strings or numbers.
# Arrays and elements do not need to be declared.
# All arrays are associative.
# Iterate with: for(variable in array).
# Delete element: delete array[subscript].
# Array["one"] = 2.
# Array[5] = "two".

# FIELD MANIPULATION

# Fields can be specified by expression: $(NF-1) is second to last, $NF is last.
# A field variable referencing a non-existent field can be created through assignment. Initial value is string: $(NF+1) = $(NF-1) / 1000.

# CAVEATS
########
# awk "{ $1 = $1 }1" file.txt ==> awk "{ $1 = $1 }; { print }" file.txt => take first column and assign to first column. it is no-op but awk uses FS and making assignment to new field, awk is going to apply FS and strip whitespace.
########
