def get_num_words(text):
    # This function should return the number of words in the text.
    num_words = len(text.split())
    return num_words

def get_num_chars(text):
    # This function should return the number of each character in the text.
    chars_count = {}
    lower_text = text.lower()
    # Convert the text to lowercase to count characters case-insensitively
    for char in lower_text:
        if char in chars_count:
            chars_count[char] += 1
        else:
            chars_count[char] = 1
    return chars_count

def sort_char(char_count):
    char_list = []
    for char in char_count:
        char_list.append({"char": char, "num": char_count[char]})
# Define a function to tell sort() what to use for sorting
    def sort_on(dict):
        return dict["num"]

    # Sort the list in-place (note we're sorting char_list, not char_count)
    char_list.sort(reverse=True, key=sort_on)

    # Return the sorted list
    return char_list

def print_counts(char_count):
    # This function should print the character counts in a formatted way.
    for char_dict in char_count:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")