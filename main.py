from stats import get_word_count, character_counts




def get_book_text(file):
    with open(file) as f:
        return f.read()



def main():
    frankenstein = get_book_text('books/frankenstein.txt')
    print(character_counts(frankenstein))
main()