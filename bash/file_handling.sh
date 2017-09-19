### The "cat" command
# Running cat with a single file will display the file in the terminal:
cat file1

# The "output redirection operator" specifies where the output of a cat command should go.
# Here, the output of cat file1 is redirected into file2 instead of to the terminal:
cat file1 > file2

# Pipeline the file content into i.e. a filter:
cat file1 | less
# The "less" filter displays the file content in a more scrollable way if file1 is long.

# The default INPUT is the keyboard, so if none is specified, cat will wait for keyboard input, interupted by ctrl+D.
cat > file1
lalalala
ThisIsText
[ctrl+D]

# Cat can handle several input files, and will append them together:
cat file1 file2 file3 > file4

# We can also, for instance, pipeline the output to a sort filter before writing to file4:
cat file1 file2 file3 | sort > file4


# The directional operator ">" removes all previous content in the file we are writing to.
# We can use the append operator ">>" to avoid this.
cat file1 >> file2


# To write a multiline string to a file, we use the following syntax:
cat > file1 <<EOF
This
Is
Text
EOF


### Reading from file
# The read command can read from a file, line by line:
while read line
do
	echo $line
done < filename

# We can also split the line with a given "Input File Seperator":
while IFS=':' read word1 word2 word3
do
	echo $word3
done < filename
