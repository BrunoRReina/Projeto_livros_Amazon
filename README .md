# Analise de Best-Sellers da Amazon

Projeto de analise de dados em Python, utilizando um dataset do Kaggle com os
livros mais vendidos da Amazon. O objetivo e explorar o dataset para responder
perguntas sobre os livros mais populares, seus autores, generos, precos e a
evolucao dessas metricas ao longo dos anos.

## Objetivo

- Quais sao os 100 livros mais vendidos, independente do ano?
- Resumo rapido de alguns desses livros.
- Qual genero e mais comum entre os best-sellers?
- Qual autor aparece com mais frequencia no top 100?
- Qual o preco medio dos livros, geral e por genero?
- A popularidade dos livros mais vendidos aumentou ou diminuiu ao longo dos anos?

## Tecnologias utilizadas

- Python
- pandas
- matplotlib

## Como rodar o projeto

1. Crie um ambiente virtual: `python -m venv venv`
2. Ative o ambiente virtual (Windows PowerShell: `venv\Scripts\Activate.ps1`)
3. Instale as dependencias: `pip install pandas matplotlib`
4. Rode o script: `python main.py`

## Sobre os dados

Dataset: Amazon Top 50 Bestselling Books (Kaggle). Colunas: `Name`, `Author`,
`User Rating`, `Reviews`, `Price`, `Year`, `Genre`.

Como o dataset nao tem uma coluna de vendas real, o numero de **Reviews** foi
usado como proxy de popularidade/vendas em todas as analises.

Um mesmo livro pode aparecer em varios anos (por ter ficado na lista de
best-sellers por mais de um ano). No calculo do "top 100 geral", essas
duplicatas sao removidas por titulo. Nas analises de tendencia por ano, o
dataset completo (com as repeticoes) e usado, pois cada linha representa a
aparicao do livro naquele ano especifico.

## Funcoes principais

| Funcao | Descricao |
|---|---|
| `top_100_mais_vendidos(dataframe)` | Retorna os 100 livros mais vendidos, ordenados por numero de reviews. |
| `resumo_aleatorio(top100, n=3)` | Mostra um resumo de `n` livros aleatorios do top 100. |
| `genero_mais_comum(top100)` | Identifica o genero mais frequente no top 100. |
| `autor_mais_frequente(top100)` | Identifica o autor com mais livros no top 100. |
| `preco_medio(top100)` | Calcula o preco medio, geral e por genero. |
| `grafico_genero_mais_comum(top100)` | Grafico de pizza com a proporcao de livros por genero. |
| `grafico_autor_mais_frequente(top100, top_n=10)` | Grafico de barras com os autores mais frequentes. |
| `grafico_preco_medio_por_genero(top100)` | Grafico de barras com o preco medio por genero. |
| `tendencia_media_por_ano(dataframe)` | Media de reviews por ano e variacao percentual ano a ano. |
| `tendencia_do_top1_por_ano(dataframe)` | Livro nº1 de cada ano e sua evolucao ao longo do tempo. |
