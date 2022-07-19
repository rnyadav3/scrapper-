import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/"

r= requests.get(url)
htmlcontent = r.content

soup=BeautifulSoup(htmlcontent, 'html.parser')
# printsoup.prettify()

title = soup.title
# print(type(soup))
# print(type(title))
# print(type(title.string))

image = soup.find_all('img')
# print(image)
para = soup.find_all('p')
# print(para)
anc = soup.find_all('a')
# for ima in image:
     


# print(anc)

# print(soup.find('p')['class'])

# print(soup.find_all("p",class_="lead"))

all_image = set()
all_links = set()

# #print(soup.find('p').get_text())
for img in image:
    if(img != '#'):
        all_image.add((img.get('img')))
        print(all_image)
        
        
for link in anc:
    if(link.get('href') != '#'):
        linkText = link.get('href')
        all_links.add(linkText)
        # print(linkText)
        
        
navbar = soup.find(id='navbar')
for nav in navbar.strings:
    print(nav) 
    

# print(navbar)
# navbarSupportedContent = soup.find(id = 'navbarSupportedContent')
# for item in navbarSupportedContent.parent:
#     print(item.name)
    
    # print(nav)
    
    



        

    
    