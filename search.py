import requests
from bs4 import BeautifulSoup

search_term = 'flower'

url = rf'https://www.google.no/search?q={search_term}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&safe=active&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'

page = requests.get(url).text

soup = BeautifulSoup(page, 'html.parser')

print(soup)

# thumbnails = []

# for raw_img in soup.find_all('img'):
    # link = raw_img.get('src')

    # print(link)
    
    # if link and link.startswith("https://"):
    #     thumbnails.append(link)
    #     pass
    
    # pass

# print(thumbnails)