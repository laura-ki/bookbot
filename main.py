def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_number_of_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")

def main():
    book = get_book_text("books/frankenstein.txt")
    get_number_of_words(book)


main()

