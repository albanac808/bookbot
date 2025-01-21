def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    char_count = count_characters(file_contents)
    sorted_char_count = sorted(char_count.items(), key=sort_on, reverse=True)
    report(file_contents, sorted_char_count)
    
def count_words(bookfile):
    word_count = 0
    words = bookfile.split()
    for word in words:
        word_count += 1
    return word_count

def count_characters(bookfile):
    char_dict = {}
    lower_book = bookfile.lower()
    for char in lower_book:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict[1]

def report(dict, char_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(count_words(dict), "words found in the document")
    print()
    for key, value in char_list:
        if key.isalpha() == True:
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
main()