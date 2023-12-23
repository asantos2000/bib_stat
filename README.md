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

