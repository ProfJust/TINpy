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

def print_most_common(word_counter, num=5):
    items = sorted(word_counter.items(), key=second_element, reverse=True)
    for word, freq in items[:num]:
        print(freq, word, sep='\t')

def subtract(d1, d2):
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = d1[key]
    return res

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
print("----")

print_most_common(word_counter)
print("----")

# https://raw.githubusercontent.com/AllenDowney/ThinkPython/v3/words.txt
word_list = open('words.txt').read().split()
valid_words = {}
for word in word_list:
    valid_words[word] = 1
diff = subtract(word_counter, valid_words)
print_most_common(diff)


singletons = []
for word, freq in diff.items():
    if freq == 1:
        singletons.append(word)
print(singletons[-5:])

import random
words = list(word_counter)
print(f" Zufällige Wörter: {random.choice(words)}")


for i in range(6):
    word = random.choice(words)
    print(word, end=' ')

weights = word_counter.values()
random.choices(words, weights=weights)

random_words = random.choices(words, weights=weights, k=6)
print(random_words)
print(f" Zufällige Wörter gewichtet: {random_words}")