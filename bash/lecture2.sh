#!/bin/bash
# Hash is usually a comment, but specifies what program to interpret with when on first line and followed by a !
# Add a -x at the end for debuging (will print the source code line by line before execution).

# Prints:
echo "Hello world"

# Assigning variables. No need to specify type.
x="Hello world"
# Remember that spaces has a function somewhat like a comma in python, and cant be inserted anywhere.

# Using/retrieving variables:
echo $x

# Because bash interprets types for you, this may not work:
x=$x+1
echo $x    # Prints "5+1"

# The "let" command does math:
let "x+=1"
echo $x    # prints 6


# Specific declaration type:
declare -i x=5

# An important thing to remember about bash is that it doesnt consider i.e. x to be a variable (except when declared) unless you call it as $x. Otherwise it will just be a string x or something.


### Parsing command-line arguments:
# With the files comes a list of parser arguments [1, 2, 3, 4]... (ignores 0, the filename).
# $0 will always refer to the name of the file.
# $1, $2,... will refer to the first, second,... CURRENT command-line argument.
# If you shift the command-line arguments, the command-line list is PERMANENTLY shorter,
# and $0, $1,... will refer to the new first and second command-line arguments.
# The same counts for $# and $@, which only takes the remainding command-line arguments.

x=$0    # Name of program
y=$1    # First command-line argument.

# All command-line arguments in array (ignoring $0):
z=$@

# Number of commandline arguments (ignoring $0):
f=$#

# Check if a command ran successfully:
g=$?    # ==0 if the last command ran didnt return any errors.

# If you run these without assignment, they will be interpreted as commands. For instance,
$1
# will run the 1st argument as a command. Assigning them will not trigger them as a command.

# To skip to the next command-line argument, use the shift command
echo $#
shift
echo $#    # Will now be one less than above.

echo $@
shift
echo $@    # This will be one shorter.


### If-tests:
if [ $i -eq 10]; then    # Use -eq for integer comparison
...
fi

if [ "$name" == "10" ]; then
...
fi



# Executing a command + storing the results (two options):
time=$(date)
time='date'



### "Pipeline". The | command passes the output of the right command to the left one.
# Here we give the output of ls -l to the grep command, which searches for results with a speific keyword
ls -l | grep 3331

# ls -s has filesize in first colomn. sort command sorts files. Sort a bunch of files after filesize:
ls -s | sort -rn






