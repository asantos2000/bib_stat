import sys
from pybtex.database import parse_file
from collections import Counter


def main(bib_file, num_authors):
    all_authors = []

    bib_data = parse_file(bib_file)

    for _, value in bib_data.entries.items():
        authors = []

        try:
            for author in value.persons["author"]:
                authors.append(f"{author.first_names[0]}, {author.last_names[0]}")
                all_authors.extend(authors)
                # print(authors)
        except:
            authors = None

    return Counter(all_authors).most_common(num_authors)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python author_list.py <bib_file> <num_authors>")
    else:
        bib_file = sys.argv[1]
        num_keywords = int(sys.argv[2])
        print(f"Authors: {main(bib_file, num_keywords)}")
