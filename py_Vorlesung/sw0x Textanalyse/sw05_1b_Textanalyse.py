# Download Text unter https://www.gutenberg.org/cache/epub/43/pg43.txt
# https://allendowney.github.io/ThinkPython/

import os
# print("Current working directory:", os.getcwd())
import unicodedata

filename = 'dr_jekyll.txt'
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)




def clean_word(word):
    return word.strip(punctuation).lower()

def split_line(line):
    return line.replace('—', ' ').split()

def second_element(t):
    return t[1]



punc_marks = {}
with open(filename, 'r', encoding='utf-8',  errors='ignore') as file:
        for line in file:
            for char in line:
                category = unicodedata.category(char)
                if category.startswith('P'):
                    punc_marks[char] = 1
                    punctuation = ''.join(punc_marks)
        print(punctuation)


unique_words2 = {}
with open(filename, 'r', encoding='utf-8',  errors='ignore') as file:
    for line in file:
        for word in split_line(line):
            word = clean_word(word)
            unique_words2[word] = 1

    print(len(unique_words2))
    print(sorted(unique_words2, key=len)[-5:])


word_counter = {}
with open(filename, 'r', encoding='utf-8',  errors='ignore') as file:
    for line in file:
        for word in split_line(line):
            word = clean_word(word)
            if word not in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] += 1

items = sorted(word_counter.items(), key=second_element, reverse=True)
for word, freq in items[:5]:
    print(freq, word, sep='\t')