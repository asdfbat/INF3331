import red

s = "asdf ASDF AsDf asdfbat ASDFbat A$DFbat asdfbatasdfbat Adfbat bat asdf"

### Substituting ###
print(re.sub(r"asdf", "x", s))  # Use the r (raw) in fron of the string to tell python
                                # the string should be interpreted as "raw",
                                # and string-commands like \n, \b, etc won't be executed.

### Finding stuff ###
print(re.findall(r"as.fbat", s))


### Custom character class [ ] ###
# We can use a custom character class to further specify allowed characters.
# It counts as a single character, and specifies the allowed values.
regex = "[aA][sS].."   # a or A, followed by s or S, then two other characters, is allowed
print(re.findall(regex, s))

# We can also specify intervals:
regex = "[0-9]"
regex = "[A-F]"
regex = "[a-f]"
