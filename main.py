from stats import get_word_count




def get_book_text(file):
    with open(file) as f:
        return f.read()



def main():
    frankenstein = get_book_text('books/frankenstein.txt')
    word_count = get_word_count(frankenstein)
    print(str(word_count) + " words found in the document")
main()