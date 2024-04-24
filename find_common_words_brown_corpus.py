''' Problem Statement 
Write a program to find all words that occur at least three times in the Brown Corpus.
'''
import nltk
from nltk.corpus import brown
from collections import Counter

def find_common_words(corpus, min_occurrences):
words = [word.lower() for word in corpus.words()]
word_counts = Counter(words)
common_words = [word for word, count in word_counts.items() if count >=        min_occurrences]
return common_words

def main():
nltk.download('brown')
min_occurrences = 3
common_words = find_common_words(brown, min_occurrences)
print(f"Words that occur at least {min_occurrences} times in the Brown Corpus:")
print(common_words)

if __name__ == "__main__":
    main()
