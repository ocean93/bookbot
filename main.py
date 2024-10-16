def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        character_count = get_character_count(file_contents)
        char_list = dict_to_list(character_count)
        
        char_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for char_dict in char_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
        print("--- End report ---")
        

def get_word_count(file_contents):
    words = file_contents.split()
    count = len(words)
    return count

def get_character_count(file_contents):
    chars = {}
    for c in file_contents:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def dict_to_list(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    return char_list

def sort_on(dict):
    return dict["count"]

main()

"""
Alternative code bookbot:
def main()
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
"""