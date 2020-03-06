<strong>iPaper Web Scrapping</strong>

  iPaper é uma plataforma de venda online através de catálogos. O programa é feito para pegar os produtos ofertados na revista selecionada e colá-los em uma planilha Excel.

<strong>Bibliotecas utilizadas:</strong>

  • BeautifulSoup
  <br>• Urllib.Request
  <br>• Re
  <br>• Json
  <br>• Xlsxwriter
  <br>• Datetime
  
<strong>Como utilizar</strong>

  • O script precisa de três informações para poder buscar:
  
    ○ gerarArquivosExcel(self, nomeArquivo, caminhoArquivo): Nome do arquivo e onde será salvo;
    ○ buscarURL(self, url): URL onde serão buscadas as informações.
    
<strong>Output</strong>

  Será gerada uma planilha conforme abaixo:
  
  ![Alt text](https://github.com/gabriel-vinci/ipaper-web-scrapping/blob/master/output1.PNG?raw=true "Output1")
  
<strong>Observações gerais</strong>

  Esse é meu primeiro trabalho com web scrapping e, naturalmente, precisa de melhorias. O próximo passo, na minha visão, seria:
  
  • Um método de categorização dos produtos (como por exemplo 'Moda Feminina', 'Moda Masculina', 'Utilidades Cozinha', etc) e uma subcategorização (com informações como 'Vestido', 'Calça', 'Blusa', 'Panela'), para possibilitar uma análise mais completa.
 
