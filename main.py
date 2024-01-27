def read_file(path):
    with open(path) as f:
        return f.read()

def count_words(content):
    words = content.split()
    return len(words)

def count_by_letter(content):
    char_count = {}
    lower = content.lower()
    for letter in lower:
        if letter.isalpha():
            if letter in char_count:
                char_count[letter] += 1
            else:
                char_count[letter] = 1
    return char_count

def sort_by(e):
    return e["count"]

def get_sort_list(letter_dict):
    letter_list = []
    for letter in letter_dict:
        letter_list.append({"letter": letter,"count":letter_dict[letter]})
    letter_list.sort(reverse=True, key=sort_by)
    return letter_list


def main():
    content = read_file("books/frankenstein.txt")
    num_words = count_words(content)
    char_count = count_by_letter(content)
    letter_list = get_sort_list(char_count)
    print("--- Begin report for file ---")
    print(f"{num_words} words in file")
    print()
    for letter_count in letter_list:
        print(f"The '{letter_count["letter"]}' character was found {letter_count["count"]} times")
    print("--- End report ---")

main()