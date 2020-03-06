from bs4 import BeautifulSoup
import urllib.request
import re
import json
import xlsxwriter
import datetime

class buscaProdutosIpaper:
    def gerarArquivoExcel(self, nomeArquivo, caminhoArquivo):
        self.workbook = xlsxwriter.Workbook(caminhoArquivo + nomeArquivo + '.xlsx')
        self.worksheet = self.workbook.add_worksheet('Produtos')
        self.worksheet.write(0, 0, "Tamanho")
        self.worksheet.write(0, 1, "Código")
        self.worksheet.write(0, 2, "Página")
        self.worksheet.write(0, 3, "Preço")
        self.worksheet.write(0, 4, "Nome")
        print(f'Arquivo {nomeArquivo} foi gerado.\n')

    def buscarURL(self, url):
        print('Buscando...')
        try:
            conexao = urllib.request.urlopen(url)
            js = conexao.read()
            soup = BeautifulSoup(js, "html.parser")
            data = str(soup.find_all("script"))
            regex = re.findall('(https://)([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', data)
            self.res = [''.join(tups) for tups in regex]
        except:
            print('Erro! Verificar URL.')

    def buscarProdutos(self):
        linha = 1
        pagina = 1
        try:
            for i in range(0, 12):
                produtos = urllib.request.urlopen(self.res[i])
                soupUm = BeautifulSoup(produtos, "html.parser")
                texto = json.loads(str(soupUm))
                valores = texto.get("enrichments")

                for j in range(len(valores)):
                    valoresUm = valores[j]

                    try:
                        for b in valoresUm:
                            self.worksheet.write(linha, 0, valoresUm['desc'])
                            self.worksheet.write(linha, 1, valoresUm['productId'])
                            self.worksheet.write(linha, 2, valoresUm['pagenumber'])
                            self.worksheet.write(linha, 3, valoresUm['price'])
                            self.worksheet.write(linha, 4, valoresUm['name'])
                    except:
                        continue
                    linha += 1

                    if pagina != valoresUm['pagenumber']:
                        pagina = valoresUm['pagenumber']

                print(f'Os produtos até a página {pagina} foram registrados.')
        except:
            print("URL com erro.")

        self.workbook.close()

print('\n \n *** IPAPER WEB SCRAPPING *** \n \n')
a = datetime.datetime.now()
print(f'O script começou as: {a}\n')

search = buscaProdutosIpaper()
search.buscarURL('http://catalogos.hiroshima.com.br/11-12/hiroshima/?page=1#/')
search.gerarArquivoExcel('Hiroshima 01-02', '')
search.buscarProdutos()

print('\nFinalizado!')

b = datetime.datetime.now()
print(f'O script levou {b-a} para concluir a busca.')
