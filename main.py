def open_book(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book):
    words = book.split()
    return len(words)

def dict_char_count(book):
    dict_char = {}
    for char in book:
        low_char = char.lower()
        if low_char in dict_char:
            dict_char[low_char] += 1
        else:
            dict_char[low_char] = 1
    return dict_char

def sort_on(dict):
    return dict["count"]

def main():
    book_path = "books/frankenstein.txt"
    text = open_book(book_path)
    dict_char = dict_char_count(text)
    chars = []
    for char in dict_char:
        if char.isalpha(): chars.append({"char":char, "count":dict_char[char]})
    chars.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words found in the document")
    for dict in chars:
        char = dict["char"]
        count = dict["count"]
        print(f"The {char} character was found {count} times")
    print("--- End report ---")

    
main()