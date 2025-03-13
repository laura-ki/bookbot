def get_number_of_words(book_text):
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def get_characters(book_text):
    character_dictionary = {}
    for sym in book_text:
        low_sym = sym.lower()
        if low_sym in character_dictionary:
            character_dictionary[low_sym] = character_dictionary[low_sym] + 1
        else:
            character_dictionary[low_sym] = 1
    return character_dictionary

def sort_on(dict):
    return dict["count"]

def sort_characters(dictionary):
    character_list = []
    for character in dictionary:
        count = dictionary[character]
        kzn = {"character": character, "count": count}
        character_list.append(kzn)
    character_list.sort(reverse=True, key=sort_on)
    return character_list