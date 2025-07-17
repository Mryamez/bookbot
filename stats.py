def get_word_count(text):
    return len(text.split())

def character_counts(text):
    text = text.lower()
    chars = {}

    for i in text:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    
    return chars

def sort_chars(dictionary):
    char_list = []

    for k, v in dictionary.items():
        if k.isalpha():
            char_list.append({"char":k, "num":v})
    
    char_list.sort(reverse=True, key = lambda items:items["num"])
    return char_list