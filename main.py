def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End Reports ---")

def list_of_dict(dict_to_list):
    length = len(dict_to_list)
    key_list = ["char", "number"]
    result = []
    for i in range(0, length):
        result.append({key_list[0]: dict_to_list[i], key_list[1]: dict_to_list[i+1]})
    
    return result

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list

def get_num_words(text):
    words = text.split()
    
    return len(words)

def get_char_dict(text):
    chars = {}
    
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    
    return chars

def get_text(path):
    with open(path) as f:
        return f.read()

main()