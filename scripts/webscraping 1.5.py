from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'http://127.0.0.1:5000/complaints'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

#v1
#with open('quotes.csv', 'w', newline='', encoding='utf-8')as f:
#    thewriter = writer(f)
    #pegando os dados
#    for p in soup.find_all('p'):
#        texto = p.get_text()
#    for h5 in soup.find_all('h5'):
#        autor = h5.get_text()
#    formataçao = [ autor,  texto]
#   thewriter.writerow(formataçao)


#v2
with open('quotes.csv', 'w', newline='', encoding='utf-8') as f:
    thewriter = writer(f)
    thewriter.writerow(['Autor', 'Texto'])
    for autor in soup.find_all('h5'):
        autores = autor.get_text()
    for texto in soup.find_all('p'):
        textos = texto.get_text()
    formataçao = [autores, textos]
    thewriter.writerow(formataçao)

print("✅ CSV gerado com sucesso!")
