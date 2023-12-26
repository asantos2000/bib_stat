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
# Keywords in abstract: [('natural language', 51), ('large language', 20), ('verlag berlin', 15), ('g .,', 14), ('business rules', 11), ('legal documents', 10), ('legal information', 9), ('https ://', 9), ('defeasible deontic', 9), ('legal reasoning', 8)]
# Keywords in title: [('natural language', 13), ('legal documents', 11), ('large language', 10), ('finsim', 9), ('nlp', 8), ('ontology', 8), ('legal domain', 8), ('review', 7), ('legal texts', 7), ('knowledge graphs', 7)]
# Keywords in keyword: [('natural language processing', 31), ('sbvr', 25), ('ontology', 21), ('deep learning', 17), ('business rules', 14), ('information extraction', 12), ('nlp', 10), ('machine learning', 10), ('deontic logic', 10), ('semantic web', 10)]
# Authors: [('Dieuwke, Hupkes', 41), ('Mario, Giulianelli', 39), ('Verna, Dankers', 37), ('Mikel, Artetxe', 35), ('Yanai, Elazar', 33), ('Tiago, Pimentel', 31), ('Christos, Christodoulopoulos', 29), ('Karim, Lasri', 27), ('Naomi, Saphra', 25), ('Alexa, Siu', 24)]
# Years: [('2023', 100), ('2022', 40), ('2021', 34), ('2019', 33), ('2020', 28), ('2017', 14), ('2013', 13), ('2018', 13), ('2012', 11), ('2011', 10)]
# In the data/many_entries.bib the oldest: 1913 - Newest: 2024
```

Isso analisará o arquivo .bib especificado e exibirá as 10 palavras-chave mais comuns no título, resumo e seção de palavras-chave, os 10 autores mais comuns e os 10 anos mais comuns de publicação.

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

