import sys
from pybtex.database import parse_file
from collections import Counter


def main(bib_file, num_years):
    all_years = []

    bib_data = parse_file(bib_file)

    for key, value in bib_data.entries.items():
        key = key
        year = value.fields['year']
        all_years.append(year)

    return Counter(all_years).most_common(num_years), min(all_years), max(all_years)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python year_list.py <bib_file> <num_years>")
    else:
        bib_file = sys.argv[1]
        num_keywords = int(sys.argv[2])
        ret = main(bib_file, num_keywords)
        print(f'Years: {ret[0]}')
        print(f'In the {sys.argv[1]} the oldest: {ret[1]} - Newest: {ret[2]}')
