from bs4 import BeautifulSoup

import requests

url = "https://www.iplt20.com/stats/2025"

response = requests.get(url)

html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.find_all('div', class_ = 'nextStoryBtn'))

# details = soup.select('.nextStoryBtn > img')

# print(details)

# print(soup)

details = soup.select('.new-video-share > span' )

detals_a = soup.select('.new-video-share > a')

print(details, detals_a)

# print(details)

# print(response.text)

# print(soup.prettify())

# html_doc = """ 

# <html>
# <head>
# <title>My first Website</title>
# </head>
# <body>
# <h2>I AM JITTU</h2>
# <p>This is my first paragraph</p>
# <a href="www.google.com">google</a>
# </body>
# </html>

# """

# soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.title.string)
# print(soup.find('p').string)
# print(soup.find('a').get('href'))