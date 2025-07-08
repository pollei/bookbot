#! /usr/sbin/python

# print("greetings boots")
from stats import count_words_in_txt, count_letter_freq_in_txt, sorted_letter_freq_in_txt
import sys

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    # do something with f (the file) here
    return file_contents

def book_report(file_path):
  txt = get_book_text(file_path)
  word_cnt = count_words_in_txt(txt)
  sorted_letts = sorted_letter_freq_in_txt(txt)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  print("---------- Word Count ----------")
  print(f"Found {word_cnt} total words")
  print("--------- Character Count -------")
  for lett_freq in sorted_letts:
    print(f"{lett_freq['char']}: {lett_freq['num']}")

def main_old():
  txt = get_book_text("books/frankenstein.txt")
  word_cnt = count_words_in_txt(txt)
  print(f"{word_cnt} words found in the document")
  #lett_cnts = count_letter_freq_in_txt(txt)
  #print(lett_cnts)
  sorted_letts = sorted_letter_freq_in_txt(txt)
  print(sorted_letts)


def main():
  if len(sys.argv) <2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_report(sys.argv[1])


main()

