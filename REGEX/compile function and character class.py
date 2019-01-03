import re


# re.compile(pattern)      ---returns a regex object

regex = re.compile('[^a-zA-Z]')

# regex.match(string to match) --return None if no match else returns a match object

#print(regex.match('ab'))

# character class
#print(regex.match('bc'))


# complement the set [^pattern]
print(regex.match('*'))

# all metacharacters lose their meaning inside a character class