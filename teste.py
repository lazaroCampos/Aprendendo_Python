from bs4 import BeautifulSoup

# Imagine que este HTML veio de um site de loja
html_simulado = """
<div class="cartao-produto">
    <h2 class="titulo">Cadeira Ergonômica</h2>
    <p class="descricao">Conforto para seu home office.</p>
    <span class="preco-final">R$ 850,00</span>
</div>
"""

# Aqui o BeautifulSoup organiza esse HTML
soup = BeautifulSoup(html_simulado, 'html.parser')

# 1. Buscamos a tag 'span' que tem a classe 'preco-final'
elemento_preco = soup.find('span', class_='preco-final')

# 2. Imprimimos apenas o texto que está dentro dela
print(elemento_preco.text)