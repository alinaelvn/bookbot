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

def sort_on(item):
    return item["num"]

def sort_characters(char_counts):
    sorted_chars = [{"char": char, "num": count} for char, count in char_counts.items()]
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

    