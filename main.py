from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_text = get_book_text("books/frankenstein.txt")

    num_words = count_words(book_text)
    print (f"{num_words} words found in the document")
    
    char_count = count_characters(book_text)
    sorted = sort_characters(char_count)
    
    # report

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")




if __name__ == "__main__":
    main()
