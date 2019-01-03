from bs4 import BeautifulSoup

def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

title = soup.title

parent = title.parent
#print(parent.name)    # .name ----tag's name

# .parent
p = soup.p
print(p.parent.name)


# html  --returns us all the children of the said tag --generator

html = soup.html

print(type(html.parent))     # bs4 ----html----head...


# soup

print(soup.parent)