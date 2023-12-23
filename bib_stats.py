import sys
from pybtex.database import parse_file
import nltk
from rake_nltk import Rake
from collections import Counter

nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)


def extract_keyword(text):
    r = Rake()
    r.extract_keywords_from_text(text)
    keywordList = []
    rankedList = r.get_ranked_phrases_with_scores()
    for keyword in rankedList:
        keyword_updated = keyword[1].split()
        keyword_updated_string = " ".join(keyword_updated[:2])
        keywordList.append(keyword_updated_string)
        if len(keywordList) > 9:
            break

    return keywordList


def process_entries(bib_file):
    bib_data = parse_file(bib_file)
    all_years = []
    all_authors = []
    all_keywords = []
    all_keywords_title = []
    all_keywords_abstract = []

    for _, value in bib_data.entries.items():
        # Years
        year = value.fields["year"]
        all_years.append(year)
        # Authors
        authors = []
        try:
            for author in value.persons["author"]:
                authors.append(f"{author.first_names[0]}, {author.last_names[0]}")
                all_authors.extend(authors)
        except:
            authors = None
        # Keywords
        try:
            keywords = value.fields["keywords"].split(",")
            all_keywords.extend(list(map(lambda x: x.lower(), keywords)))
        except:
            keywords = None
        # Title
        title = value.fields["title"]

        kw = extract_keyword(title)
        all_keywords_title.extend(list(map(lambda x: x.lower(), kw)))
        # Abstract
        try:
            abstract = value.fields["abstract"]
            kw = extract_keyword(abstract)
            all_keywords_abstract.extend(list(map(lambda x: x.lower(), kw)))
        except:
            abstract = None
    return (
        all_years,
        all_authors,
        all_keywords,
        all_keywords_title,
        all_keywords_abstract,
    )


def most_common(items, num):
    return Counter(items).most_common(num)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bib_stats.py <bib_file> <num>")
    else:
        bib_file = sys.argv[1]
        num = int(sys.argv[2])

        (
            all_years,
            all_authors,
            all_keywords,
            all_keywords_title,
            all_keywords_abstract,
        ) = process_entries(bib_file)

        print(f"Keywords in abstract: {most_common(all_keywords_abstract, num)}")

        print(f"Keywords in title: {most_common(all_keywords_title, num)}")

        print(f"Keywords in keyword: {most_common(all_keywords, num)}")

        print(f"Authors: {most_common(all_authors, num)}")

        ret = most_common(all_years, num), min(all_years), max(all_years)
        print(f"Years: {ret[0]}")
        print(f"In the {sys.argv[1]} the oldest: {ret[1]} - Newest: {ret[2]}")
