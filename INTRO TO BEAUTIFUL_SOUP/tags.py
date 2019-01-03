from bs4 import BeautifulSoup

def read_file():
    file = open('tags.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(), 'lxml')

#Accessing tags

meta = soup.meta

#tag methods

print(meta.get('charset'))
