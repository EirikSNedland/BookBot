def main():
    file_path = "books/Frankenstein.txt"
    file_content = get_file_content(file_path)
    len_word = get_word_len(file_content)
    char_dict_number = amount_each_letter(file_content)
    sorted_list = sort_dict(char_dict_number)
    print("----- Report on: " + file_path + " -----")
    print("word count: " + str(len_word))
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"'{item["char"]}' appered in the file '{item["num"]}'times")
    print("----- End Report -----")


def get_file_content(file_path):
    with open(file_path) as f:
        return f.read()

def print_text_from_file(file_content):
    print(file_content)

def get_word_len(file_content):
    words = file_content.split()
    return len(words)

def amount_each_letter(file_content):
    lowered_string = file_content.lower()
    letter_dict = {}
    for letter in lowered_string:
        if letter in letter_dict.keys():
            letter_dict[letter] = letter_dict[letter] + 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sort_dict(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char":ch , "num":dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

main()