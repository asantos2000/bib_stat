from dataclasses import fields
from pybtex.database import parse_file
import nltk

def most_common_words(value):
    allWords = nltk.tokenize.word_tokenize(value)
    allWordDist = nltk.FreqDist(w.lower() for w in allWords)

    stopwords = nltk.corpus.stopwords.words('english')
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)

    return allWordExceptStopDist.most_common(10)

bib_data = parse_file('many_entries_2.bib')
for key, value in bib_data.entries.items():
    authors = []
    key = key
    title = value.fields['title']
    year = value.fields['year']
    try:
        for author in value.persons['author']:
            authors.append(f'{author.first_names[0]}, {author.last_names[0]}')
    except:
        auhtors = None
    try:
        keywords = value.fields['keywords']
    except:
        keywords = None
    
    print(f'{key} - {title}, {year}, {authors}, keywords: {keywords}')
