from bs4 import BeautifulSoup

def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

# .contents    --returns us direct children of the said tag

#head = soup.head
#print(head.contents)

#print(len(head.contents))

for child in soup.head:
    #print(child)
    pass

# .descendents  --returns us all the children of the said tag --generator

for index,child in enumerate(soup.head.descendants):
    print(index)
    print(child if child != '\n' else '')