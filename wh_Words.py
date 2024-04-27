import nltk
from nltk import word_tokenize

f = open('corpus.txt')
raw = f.read()

# tokenizes that text
tokens = word_tokenize(raw)

# pulls out all the words that start with wh. and prints it out.
wh_words = [word for word in tokens if word.startswith('wh')]

# sorts the list and prints it
wh_words.sort()
print(wh_words)
