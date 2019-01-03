from bs4 import BeautifulSoup
import re


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')

# Signature: find_all(name, attrs, recursive, string, limit, **kwargs)

# name parameter


# regex object -string -True -function

a_tags = soup.find_all('a')

for a in a_tags:
    # print(a)
    pass


# attrs parameter

# dictionary

attr = {'class': 'sister', 'id': 'link1'}    # can also do attr = {'class': 'sister'}
first_a = soup.find_all('a', attrs=attr)
# print(first_a)


# limit parameter

a_tags = soup.find_all('a', limit=1)
print(a_tags)
