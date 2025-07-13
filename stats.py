def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    book_text = book_text.lower()
    char_counts = {}

    for char in book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts