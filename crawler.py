from bs4 import BeautifulSoup
import requests

url = input('Digite a URL do site a ser analisado: ')

if url is None or url == '':
    url = 'http://tableless.com.br'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print('\nVocê está executando uma crawler na página do "' + soup.title.string + '"!\n')

element_search = input('Digite a tag a ser procurada (e.g.: body, div, p): ')

elements = [ element.text for element in soup.findAll(element_search) ]

if len(elements) > 0:
    print('\nElementos com a tag "' + element_search + '"...')

    for element in elements:
        print(element)
else:
    print('\nTag não encontrada na página!')
