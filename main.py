from stats import get_number_of_words
from stats import get_characters
from stats import sort_characters

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    word_num = get_number_of_words(book)
    characters = get_characters(book)
    sorted_ch = sort_characters(characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")
    for i in sorted_ch:
        if i["character"].isalpha():
            print(f"{i["character"]}: {i["count"]}")
    print("============= END ===============")


main()

