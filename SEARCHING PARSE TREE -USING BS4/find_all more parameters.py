from bs4 import BeautifulSoup
import re


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')

# Signature: find_all(name, attrs, recursive, string, limit, **kwargs)

# string parameter

regex = re.compile('Elsie')

tag = soup.find_all(string=regex)
# print(tag)


# **kwargs arguments

tags = soup.find_all(class_='sister')
# print(len(tags))

# to write the class attribute of a tag - use


# recursive parameter

title = soup.find_all('title', recursive=False)
print(title)    # if recursive=True or nothing(it takes default as true) so it will be finding title in whole html
