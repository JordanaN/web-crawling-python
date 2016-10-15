from bs4 import BeautifulSoup
import requests


class Item(object):
    def __init__(self, language, stars, forks):
        self.language = language
        self.stars = stars
        self.forks = forks


url = 'https://github.com/showcases/programming-languages'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

items = soup.find_all("li", class_="repo-list-item")

components = []

for item in items:
    info = list(filter(None, item.div.get_text().split('\n')))
    info = list(filter(None, [i.strip() for i in info]))

    if len(info) == 2:
        language = None
    else:
        language = info[0]

    stars = int(info[0 if len(info) == 2 else 1].replace(',', ''))
    forks = int(info[1 if len(info) == 2 else 2].replace(',', ''))

    components.append(Item(language, stars, forks))
