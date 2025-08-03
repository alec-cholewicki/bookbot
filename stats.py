def get_book_words(book_text):
    words = book_text.split()
    return len(words)
def get_book_characters(book_text):
    character_dict = {}
    for character in book_text:
        lowercased_character = character.lower()
        if lowercased_character in character_dict:
            character_dict[lowercased_character] += 1
        else:
            character_dict[lowercased_character] = 1
    return character_dict
def sort_dicts(input_dict):
    def sort_on(item):
        return item["num"]

    dict_list = []
    for character in input_dict:
        character_dict = {
            "char": character,
            "num": input_dict[character]
        }
        dict_list.append(character_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
