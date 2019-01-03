from bs4 import BeautifulSoup

def read_file():
    file = open('three_sisters.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')

body = soup.body
p = soup.p

# body - contents

#print(body.contents)

# .next_siblings

print(p)
print('\n\n')
print(p.next_sibling.next_sibling)