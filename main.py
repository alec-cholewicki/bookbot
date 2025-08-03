import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("---------- Word Count ----------")
    book_path = sys.argv[1]
    number_of_words = get_book_words( get_book_text(book_path))
    print (f"Found {number_of_words} total words")
    print("---------- Character Count ----------")
    characters = sort_dicts(get_book_characters( get_book_text(book_path)))
    for character in characters:
        if character["char"].isalpha() == True:
            print(f"{character["char"]}: {character["num"]}")
    print("========== END ==========")
   

from stats import get_book_words
from stats import get_book_characters
from stats import sort_dicts
main()
