def get_number_of_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    print(f"{word_count} words found in the document")

def get_characters(book_text):
    character_dictionary = {}
    for sym in book_text:
        low_sym = sym.lower()
        if low_sym in character_dictionary:
            character_dictionary[low_sym] = character_dictionary[low_sym] + 1
        else:
            character_dictionary[low_sym] = 1
    return character_dictionary

