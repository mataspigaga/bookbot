import sys
from stats import get_num_words, get_num_chars, process_char_count

def get_book_text(file_path):
    with open(file_path) as f:
        text = f.read() 
    return text

def main():
    if len(sys.argv) <= 1:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dict_chars = get_num_chars(text)
    sorted_list = process_char_count(dict_chars)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for item in sorted_list:
        print(f'{item['char']}: {item['num']}')
    print('============= END ===============')

main()
