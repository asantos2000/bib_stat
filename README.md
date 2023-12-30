# Estatísticas Bib

Este projeto é uma ferramenta de linha de comando que analisa arquivos .bib (BibTeX) para extrair estatísticas úteis, como os autores mais comuns, as palavras-chave mais comuns no título, resumo e seção de palavras-chave, e a distribuição de anos de publicação.

## Instalação

Para instalar e executar este projeto, você precisará ter Python 3 e pip instalados em seu sistema.

1. Clone o repositório:

```bash
git clone https://github.com/seu_usuario/bib_stats.git
cd bib_stats
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Uso

Para usar esta ferramenta, você precisa ter um arquivo .bib que deseja analisar. Você pode executar o script `bib_stats.py` passando o caminho para o arquivo .bib e o número de itens mais comuns que você deseja exibir. Por exemplo:

```bash
python bib_stats.py data/many_entries.bib 10

# Output
# Keywords in abstract: [('paper present', 43), ('verlag berlin', 10), ('paper propose', 9), ('based method', 8), ('recent year', 7), ('based model', 7), ('experimental result', 7), ('ccs concepts', 7), ('based approach', 6), ('also present', 6)]
# Keywords in title: [('natural language', 7), ('ontology', 5), ('named entity', 4), ('bert', 4), ('2 task', 4), ('multi', 3), ('corpus automatic', 3), ('deontic ambiguities', 3), ('finsim', 3), ('survey', 3)]
# Keywords in keyword: [('natural language processing', 31), ('sbvr', 25), ('ontology', 21), ('deep learning', 17), ('business rules', 14), ('information extraction', 11), ('nlp', 10), ('machine learning', 10), ('deontic logic', 10), ('semantic web', 10)]
# Authors: [('Dieuwke, Hupkes', 41), ('Mario, Giulianelli', 39), ('Verna, Dankers', 37), ('Mikel, Artetxe', 35), ('Yanai, Elazar', 33), ('Tiago, Pimentel', 31), ('Christos, Christodoulopoulos', 29), ('Karim, Lasri', 27), ('Naomi, Saphra', 25), ('Alexa, Siu', 24)]
# Years: [('2023', 94), ('2022', 39), ('2021', 33), ('2019', 29), ('2020', 27), ('2013', 12), ('2018', 12), ('2017', 12), ('2012', 11), ('2008', 9)]
# In the data/many_entries.bib the oldest: 1913 - Newest: 2024
```

Isso analisará o arquivo .bib especificado e exibirá as 10 palavras-chave mais comuns no título, resumo e seção de palavras-chave, os 10 autores mais comuns e os 10 anos mais comuns de publicação.

## Bertopic

O notebook topic-modeling-bibtext-entries.ipynb usa a biblioteca `bertopic` para gerar tópicos a partir dos resumos dos artigos. O notebook está configurado para usar o arquivo `data/many_entries.bib` como entrada. Você pode alterar o arquivo de entrada para o que desejar.

Versão no Kaggle: <https://www.kaggle.com/code/adsantos/topic-modeling-bibtex-entries>

## Problemas comuns

A biblioteca pybtex retornará um erro se a as entradas no arquivo bibtext forem vazias ou repitidas.

Exemplos:

```bash
python bib_stats.py data/many_entries_fault.bib 5 

# Entrada duplicada
Traceback (most recent call last):
...
pybtex.database.BibliographyDataError: repeated bibliograhpy entry: Goossens2022

# Entrada vazia
python bib_stats.py data/one_entry_fault.bib 5

Traceback (most recent call last):
...
pybtex.scanner.TokenRequired: syntax error in line 1: entry key expected
```

## Arquivos bibtext de exemplo

Os arquivos bibtex de exemplo foram gerados pela função de _export_ do [Mendeley](https://www.mendeley.com/).

## Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para abrir uma issue ou enviar um pull request.

