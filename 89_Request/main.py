import requests
'''
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    "title":"harry",
    "body":'bhai',
    "userId":12
}
headers = {'Content-type':'application/json ; charset= utf-8'}
response = requests.post(url, headers = headers, json = data)
print(response.text)
'''

from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/djnago-cheatsheet/"
r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())

for heading in soup.find_all('h2'):
    print(heading.text)


