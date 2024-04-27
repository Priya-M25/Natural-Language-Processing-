import nltk
from nltk.corpus import brown

def word_freq(word, genre):
fdist = nltk.FreqDist([w.lower() for w in nltk.corpus.brown.words(categories=genre)])
print(f"The word '{word}' appears {fdist[word]} times in the '{genre}' genre of the Brown Corpus.")

# Example usage:
word_freq('the', 'religion')
