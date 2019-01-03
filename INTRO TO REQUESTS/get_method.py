import requests  #import module

#requests.get(url)   --response object

response = requests.get('https://nikhil068.pythonanywhere.com/login/')
#print(response)

#content

#response.content

#print(response.content)

#headers returned
#response.headers

#print(response.status_code)

# print(response.headers)
#
for key,value in response.headers.items():
    print(key, '   ',value)