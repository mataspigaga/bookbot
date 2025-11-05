def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    chars_dict = {}
    for c in text:
        char = c.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(items):
    return items['num']

def process_char_count(dict):
    new_list = []
    for k in dict:
        if not k.isalpha():
            continue
        new_list.append(
            {
                'char': k,
                'num': dict[k]
            }
        )
    new_list.sort(reverse=True, key=sort_on)
    return new_list