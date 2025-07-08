#! /usr/sbin/python

def count_words_in_txt(text_str):
  words = text_str.split()
  return len(words)

def count_letter_freq_in_txt(text_str):
  lett_cnts = {}
  for lett_raw in text_str:
    lett = lett_raw.lower()
    if not lett in lett_cnts:
      lett_cnts[lett]=0
    lett_cnts[lett]+=1
  return lett_cnts

def sort_on(items):
    return items["num"]

def sorted_letter_freq_in_txt(text_str):
  lett_cnts = count_letter_freq_in_txt(text_str)
  lett_arr = []
  for lett in lett_cnts:
    if not lett.isalpha(): continue
    lett_arr.append({
      "char": lett,
      "num": lett_cnts[lett] })
  lett_arr.sort(key=sort_on, reverse=True)
  return lett_arr
