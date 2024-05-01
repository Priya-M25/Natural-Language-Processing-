import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def apply_stemming(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Initialize the Porter Stemmer
    porter_stemmer = PorterStemmer()

    # Apply stemming to each word
    stemmed_words = [porter_stemmer.stem(word) for word in words]

    # Join the stemmed words back into a sentence
    stemmed_sentence = ' '.join(stemmed_words)

    return stemmed_sentence

def main():
    # Example sentence
    input_sentence = "Stemming is an important step in natural language processing."

    # Apply stemming to the sentence
    stemmed_result = apply_stemming(input_sentence)

    # Display the results
    print("Original Sentence:")
    print(input_sentence)
    print("\nStemmed Sentence:")
    print(stemmed_result)

if __name__ == "__main__":
    main()


'''Output :-

'''
