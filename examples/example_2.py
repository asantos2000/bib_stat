from dataclasses import fields
from pybtex.database import parse_file
bib_data = parse_file('one_entry.bib')
print(bib_data.entries['Maynard2020'].fields['title'])
# for author in bib_data.entries['Knuth:TB8-1-14'].persons['author']:
#     print(unicode(author))
print(bib_data.entries['Maynard2020'].fields['abstract'])