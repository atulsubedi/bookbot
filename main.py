def main():
  path = open_book("books/frankenstein.txt")  
  words = num_of_word_of_books(path)
  word_dict = count_each_words(path)
  dict_sorted_list = chars_dict_to_sorted_list(word_dict)
  
  print(f"--- Begin report of the book ---")
  print(f"There are {words} in the book")
  print()
  for item in dict_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

  print("--- End report ---") 

def open_book(path):
    with open(path) as f:
     return  f.read()

def num_of_word_of_books(txt):
    words = txt.split()
    return len(words)

def count_each_words(txt):
    word = {}
    for c in txt:
        lowered = c.lower()
        if lowered in word:
            word[lowered] += 1
        else:
            word[lowered] = 1
    return word
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()