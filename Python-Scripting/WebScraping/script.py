from bs4 import BeautifulSoup

html.doc = """ 

<html>
<head>
<title>My first Website</title>
</head>
<body>
<h2>I AM JITTU</h2>
<p>This is my first paragraph</p>
</body>
</html>

"""

soup = BeautiSoup(html.doc, 'html.parser')

print(soup.title.string)