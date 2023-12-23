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


def main(bib_file, num_keywords):
    all_keywords = []

    bib_data = parse_file(bib_file)

    for _, value in bib_data.entries.items():
        try:
            abstract = value.fields["abstract"]
            kw = extract_keyword(abstract)
            all_keywords.extend(list(map(lambda x: x.lower(), kw)))
        except:
            abstract = None

    return Counter(all_keywords).most_common(num_keywords)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python keyword_extractor.py <bib_file> <num_keywords>")
    else:
        bib_file = sys.argv[1]
        num_keywords = int(sys.argv[2])
        print(f"Keywords: {main(bib_file, num_keywords)}")
