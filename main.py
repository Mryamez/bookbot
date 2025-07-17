import sys
from stats import get_word_count, character_counts, sort_chars




def get_book_text(file):
    with open(file) as f:
        return f.read()



def main():
    frankenstein = get_book_text('books/frankenstein.txt')
    characters = sort_chars(character_counts(frankenstein))

    print("============ BOOKBOT ============")
    print("Analyzing book found at at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found " + str(get_word_count(frankenstein)) + " total words")
    print("--------- Character Count -------")
    
    for i in characters:
        print(i["char"] + ": " + str(i["num"]))
    
    print("============= END ===============")
main()