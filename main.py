import pandas as pd  #Utilizando a biblioteca no projeto
import matplotlib.pyplot as plt


df = pd.read_csv('dados/Mais_vendidos_por_categoria.csv') #Lendo o arquivo do Dataset
df_unico = df.drop_duplicates(subset='Name') #Excluindo Duplicatas


def top_100_mais_vendidos(dataframe):  #Seleciona e filtra os 100 livros mais vendidos do Dataset
    top100 = dataframe.sort_values(by='Reviews', ascending=False).head(100)
    return top100.reset_index(drop=True)


def resumo_aleatorio(top100, n=5):#Seleciona aleatóriamente 3 livros do top 100 e resume as informações
    escolhidos = top100.sample(n=n)
    for _, livro in escolhidos.iterrows():
        print(f"📖 {livro['Name']}")
        print(f"   Autor: {livro['Author']}")
        print(f"   Gênero: {livro['Genre']}")
        print(f"   Ano: {livro['Year']}")
        print(f"   Avaliação: {livro['User Rating']} ⭐ | Reviews: {livro['Reviews']}")
        print(f"   Preço: ${livro['Price']}")
        print("-" * 40)


def genero_mais_comum(top100): #Filtrando os gêneros mais comuns no top 100
    contagem = top100['Genre'].value_counts()
    genero_top = contagem.idxmax()
    quantidade = contagem.max()
    print(f"Gênero mais comum: {genero_top} ({quantidade} livros)")
    print(contagem)
    return genero_top


def autor_mais_frequente(top100): #Filtrando o/a autor(a) com mais livros no top 100
    contagem = top100['Author'].value_counts()
    autor_top = contagem.idxmax()
    quantidade = contagem.max()
    print(f"Autor com mais livros no top 100: {autor_top} ({quantidade} livros)")
    print(contagem.head(10))
    return autor_top


def preco_medio(top100): #Filtrando o preço médio dos livros no top 100
    media_geral = top100['Price'].mean()
    print(f"Preço médio geral: ${media_geral:.2f}")

    media_por_genero = top100.groupby('Genre')['Price'].mean()
    print("\nPreço médio por gênero:")
    print(media_por_genero)

    return media_geral


def grafico_genero_mais_comum(top100):
    """Gera um gráfico de pizza com a proporção de livros por gênero no top 100."""
    contagem = top100['Genre'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(
        contagem,
        labels=contagem.index,
        autopct='%1.1f%%',
        colors=['steelblue', 'darkorange'],
        startangle=90
    )
    plt.title('Proporção de livros por gênero (Top 100)')
    plt.tight_layout()
    plt.show()


def grafico_autor_mais_frequente(top100, top_n=10):
    """Gera um gráfico de barras com os autores mais frequentes no top 100."""
    contagem = top100['Author'].value_counts().head(top_n)
    contagem.plot(kind='barh', color='darkorange')
    plt.title(f'Top {top_n} autores mais frequentes (Top 100)')
    plt.xlabel('Quantidade de livros')
    plt.gca().invert_yaxis()  # deixa o maior no topo
    plt.tight_layout()
    plt.show()


def grafico_preco_medio_por_genero(top100):
    """Gera um gráfico de barras com o preço médio por gênero no top 100."""
    media_por_genero = top100.groupby('Genre')['Price'].mean()
    media_por_genero.plot(kind='bar', color='seagreen')
    plt.title('Preço médio por gênero (Top 100)')
    plt.xlabel('Gênero')
    plt.ylabel('Preço médio ($)')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    
def tendencia_media_por_ano(dataframe):
    """
    Calcula a média de reviews por ano (proxy de popularidade/vendas)
    e mostra se aumentou ou diminuiu em relação ao ano anterior.
    """
    media_por_ano = dataframe.groupby('Year')['Reviews'].mean()
    variacao = media_por_ano.pct_change() * 100  # variação percentual ano a ano

    print("Média de reviews por ano:")
    print(media_por_ano)
    print("\nVariação percentual ano a ano:")
    print(variacao.round(2))

    media_por_ano.plot(kind='line', marker='o', color='purple')
    plt.title('Média de Reviews por Ano (proxy de vendas)')
    plt.xlabel('Ano')
    plt.ylabel('Média de Reviews')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return media_por_ano


def tendencia_do_top1_por_ano(dataframe):
    """
    Para cada ano, identifica o livro nº1 (mais reviews) e mostra
    como o número de reviews desse 'top 1' variou de ano para ano.
    """
    top1_por_ano = dataframe.loc[dataframe.groupby('Year')['Reviews'].idxmax()]
    top1_por_ano = top1_por_ano[['Year', 'Name', 'Reviews']].sort_values('Year')

    print("Livro nº1 (mais reviews) de cada ano:")
    print(top1_por_ano.to_string(index=False))

    top1_por_ano.set_index('Year')['Reviews'].plot(kind='line', marker='o', color='crimson')
    plt.title('Reviews do livro Top 1 de cada ano')
    plt.xlabel('Ano')
    plt.ylabel('Reviews do Top 1')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    return top1_por_ano

# --- Chamadas das funções (tudo depois das definições) ---

top100 = top_100_mais_vendidos(df_unico)

resumo_aleatorio(top100, n=3)
genero_mais_comum(top100)
autor_mais_frequente(top100)
preco_medio(top100)

grafico_genero_mais_comum(top100)
grafico_autor_mais_frequente(top100)
grafico_preco_medio_por_genero(top100)

tendencia_media_por_ano(df)
tendencia_do_top1_por_ano(df)
