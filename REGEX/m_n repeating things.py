import re


# ? question mark -- says the previous character can either come once or not at all

regex = re.compile('a?b')

#print(regex.match('abb'))

# {m,n} m and n are integer values --This qualifier mens there must be at least a repitions, and at most n

regex = re.compile('a{4,5}')

#print(regex.match('aaaa'))

# * {0,} ----from 0 to infinite

regex = re.compile('a{0,}')

print(regex.match('a'))


# + {1,}  ----from 1 to infinite


# ? {0,1}   -----only includes 0 or 1 nothing else
