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