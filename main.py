from stats import get_number_of_words
from stats import get_characters

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    get_number_of_words(book)
    characters = get_characters(book)
    print(characters)

main()

