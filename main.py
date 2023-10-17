def main():
  file_contents = open_book("books/frankenstein.txt")  
  words = num_of_word_of_books(file_contents)
  print(f"there are {words} in the book")
   
   
   
   
   
def open_book(path):
    with open(path) as f:
     return  f.read()

def num_of_word_of_books(txt):
    words = txt.split()
    return len(words)