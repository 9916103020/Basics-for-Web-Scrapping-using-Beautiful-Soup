import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#Background on user-agent

ua =UserAgent()

header = {'user-agent':ua.chrome}

#print(ua.chrome)

google_page = requests.get('https://www.google.com',headers=header)

soup = BeautifulSoup(google_page.content,'lxml')

print(soup.prettify())