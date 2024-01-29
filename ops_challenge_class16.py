# notes from demo/warmup time

# import mods
import nltk
import ssl
from nltk.corpus import words

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def get_words():
    nltk.download('words')
    word_list = words.words()
    # print(word_list)
    return word_list

def check_words(words):
    user_input = input("Please enter a word: ")
    if user_input in words:
        print("That word is indeed in the dictionary!")
    else:
        print("That word isn't in the dictionary.")

def load_file():
    password_list = []
    with open('rockyou.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.rstrip()
            password_list.append(line)
            print(password_list)

if __name__ == "__main__":
    ext_words = get_words()
    # print(ext_words)
    # check_words(ext_words)
    load_file()