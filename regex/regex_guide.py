import re

s = "asdf ASDF AsDf asdfbat ASDFbat A$DFbat asdfbatasdfbat Adfbat bat asdf"

regex = r"asdf" # Use the r (raw) in fron of the string to tell python the string
# should be interpreted as "raw" and string-commands like \n, \b, etc won't be executedself

### Finding stuff ###
matches = re.findall(regex, s)  # Returns a list of all mathces in string

### Substituting ###
new_s = re.sub(regex, "x", s)  # Returns a new string with all matching values substituted

# NOTES:
# In the replace section, most RegEx syntax doesn't apply, so characters
# like | $ { } etc doesn't need to be cancelled:
re.sub("\[\]", "[]", s)
# Back-refrences can be made both in the search, and the replace section:
re.sub("([A-C])\1", "\1", s)
