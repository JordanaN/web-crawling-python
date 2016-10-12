from bs4 import BeautifulSoup
import requests

url = 'http://tableless.com.br'
r = requests.get(url)
soup = BeautifulSoup(r.text)

print('Voce esta executando uma crawler na pagina do Tableless!')
response = input('Digite a tag a ser procurada no blog Tableless entre aspas: ')

tag = [title.text for title in soup.findAll(response)]



if tag:
	print('ITENS COM A TAG SELECIONADA')
	for item in tag:
	    print(item)
else: 
	print('ESSA TAG NAO EXISTE NESTA PAGINA')




