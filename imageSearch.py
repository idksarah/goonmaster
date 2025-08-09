import requests
from bs4 import BeautifulSoup

class ImageSearch:
    @staticmethod
    def getImageUrl(search_term):
        url = rf'https://www.google.no/search?q={search_term}&client=opera&hs=cTQ&source=lnms&tbm=isch&sa=X&safe=active&ved=0ahUKEwig3LOx4PzKAhWGFywKHZyZAAgQ_AUIBygB&biw=1920&bih=982'

        page = requests.get(url).text

        soup = BeautifulSoup(page, 'html.parser')

        thumbnails = []

        for raw_img in soup.find_all('img'): # only need first but will implement later idc
            link = raw_img.get('src')
            
            if link and link.startswith("https://"):
                thumbnails.append(link)
                pass
            pass

        # return thumbnails
        return thumbnails[0]
