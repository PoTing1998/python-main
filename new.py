from  bs4 import BeautifulSoup

text = """

<html>
  <head>
    <title>The Dormouse's story</title>
  </head>
  <body>
    <p class="title">
      <b> The Dormouse's story </b>
    </p>
    <p class="story">
      Once upon a time there were three little sisters; and their names were
      <a class="sister" href="http://example.com/elsie" id="link1"> Elsie </a>
      ,
      <a class="sister" href="http://example.com/lacie" id="link2"> Lacie </a>
      and
      <a class="sister" href="http://example.com/tillie" id="link3"> Tillie </a>
      ; and they lived at the bottom of a well.
    </p>
    <p class="story">...</p>
  </body>
</html>

"""


soup = BeautifulSoup(text, 'lxml')

print(soup.find("p"))
print(type(soup.find("p")))

print(soup.find(class_="story"))

print(soup.find_all("p",class_="title"))