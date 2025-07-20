from stats import get_character_counts, get_number_of_words, pretty_print, sort_on, sort, format_list
import sys
def get_book_text(f):
    with open(f) as g:
        return g.read()
    


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #print(get_book_text("books/frankenstein.txt"))
    #print(str(get_number_of_words(get_book_text("books/frankenstein.txt"))) + " words found in the document")
    character_counts = pretty_print(get_book_text(sys.argv[1]))
    print(character_counts)


main()
          