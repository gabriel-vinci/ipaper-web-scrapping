from bs4 import BeautifulSoup
import urllib.request
import re
import json
import xlsxwriter

nomeArquivo = '' #Escolher nome do arquivo que será gerado. Exemplo: 'Hiroshima 01-02'
url = '' #Informar a URL onde estão os produtos. Exemplo: http://catalogos.hiroshima.com.br/11-12/hiroshima/?page=1#/

connection = urllib.request.urlopen(url)
js = connection.read()
soup = BeautifulSoup(js, "html.parser")
data = str(soup.find_all("script"))
aaa = re.findall('(https://)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', data)
res = [''.join(tups) for tups in aaa]

workbook = xlsxwriter.Workbook(nomeArquivo + '.xlsx')
worksheet = workbook.add_worksheet('Produtos')
worksheet.write(0, 0, "Tamanho")
worksheet.write(0, 1, "Código")
worksheet.write(0, 2, "Página")
worksheet.write(0, 3, "Preço")
worksheet.write(0, 4, "Nome")
linha = 1

try:

    for i in range(0, 12):
        produtos = urllib.request.urlopen(res[i])
        soupUm = BeautifulSoup(produtos, "html.parser")
        texto = json.loads(str(soupUm))
        valores = texto.get("enrichments")

        for j in range(len(valores)):
            valoresUm = valores[j]

            try:
                for b in valoresUm:
                    worksheet.write(linha, 0, valoresUm['desc'])
                    worksheet.write(linha, 1, valoresUm['productId'])
                    worksheet.write(linha, 2, valoresUm['pagenumber'])
                    worksheet.write(linha, 3, valoresUm['price'])
                    worksheet.write(linha, 4, valoresUm['name'])

            except:
                continue

            print(f'Produto {linha}: OK')
            linha += 1

except:
    print("URL com erro.")

workbook.close()

print("Finalizado!")