import sys
from stats import get_word_count, character_counts, sort_chars




def get_book_text(file):
    with open(file) as f:
        return f.read()



def main():
    try:
        book = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    frankenstein = get_book_text(book)
    characters = sort_chars(character_counts(frankenstein))

    print("============ BOOKBOT ============")
    print("Analyzing book found at at " + book)
    print("----------- Word Count ----------")
    print("Found " + str(get_word_count(frankenstein)) + " total words")
    print("--------- Character Count -------")
    
    for i in characters:
        print(i["char"] + ": " + str(i["num"]))
    
    print("============= END ===============")
main()