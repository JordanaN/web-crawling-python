from bs4 import BeautifulSoup
import requests

url = 'https://github.com/showcases/programming-languages'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print('\nVoce esta executando uma crawler na pagina do "' + soup.title.string + '"!\n')

link = soup.find_all("span", class_="prefix")

print(link)


element_search = input('Digite a tag a ser procurada (e.g.: body, div, p): ')

elements = [ element.text for element in soup.findAll(element_search) ]

if len(elements) > 0:
    print('\nElementos com a tag "' + element_search + '"...')

    for element in elements:
        print(element)
else:
    print('\nTag nao encontrada na pagina!')
