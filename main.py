import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sort_char
from stats import print_counts

def main():
    if len(sys.argv) == 2:
        # Check if a command line argument was provided
        book_location = sys.argv[1]
        # If an argument is provided, use it as the book location
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # This is the location of the book file.
    file_contents = get_book_text(book_location)
    # This function will be called to get the text of the book.
    # this function will be called to get the word count of the text
    num_words = get_num_words(file_contents)
    char_count = get_num_chars(file_contents)
    sorted_list = sort_char(char_count)

    # Printing the results
    print("============ BOOKBOT ============")
    print(f"Analyzing the book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----------")
    print_counts(sorted_list)
    print("============= END ===============")
    
def get_book_text(path_to_file):
    # This function should return the text of the book.
    # For now, we will return a placeholder string.
    with open(path_to_file) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
        return file_contents

main()