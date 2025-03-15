import sys

from stats import get_number_of_words
from stats import get_characters
from stats import sort_characters

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    book = get_book_text(path_to_book)
    word_num = get_number_of_words(book)
    characters = get_characters(book)
    sorted_ch = sort_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")
    for i in sorted_ch:
        if i["character"].isalpha():
            print(f"{i["character"]}: {i["count"]}")
    print("============= END ===============")


main()

