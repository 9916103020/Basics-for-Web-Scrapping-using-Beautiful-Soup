import re

# special sequences

#\d    --matches any decimal digit -- [0-9]
regex = re.compile('\d')
#print(regex.match('a'))
#\D   --matches any non-digit character  --[^0-9]
regex = re.compile('\D')

#\s    --matches any non-whitespace character
regex = re.compile('\s')

#\S    --matches any non-whitespace character
regex = re.compile('\S')

#\w    --matches any alphanumeric character -- [a-zA-Z0-9]
regex = re.compile('\w')

#\W    --matches any non-alphanumeric character -- [^a-zA-Z0-9]
regex = re.compile('\W')