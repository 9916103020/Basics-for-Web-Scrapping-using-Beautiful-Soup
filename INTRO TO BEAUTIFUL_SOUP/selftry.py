import requests
from fake_useragent import  UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()

header = {'user-agent':ua.chrome}

page = requests.get('https://stackoverflow.com/questions/1900956/write-variable-to-file-including-name')

# print(page.status_code)

a=page.content

file = open('file.html','w')
file.write('a' + repr(a))
file.close()

def read_file():
    file = open('file.html')
    data = file.read()
    file.close()
    return  data

soup = BeautifulSoup(read_file(),'lxml')

head = soup.head

print(head.string)