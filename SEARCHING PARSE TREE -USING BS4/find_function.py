from bs4 import BeautifulSoup


def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file(), 'lxml')

# Signature: find(name, attrs, recursive, string, **kwargs)  --limit

# returns a single object if found  -- in case of multiple objects, it returns the first one it find

tag = soup.find('a')
print(tag)