import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
def most_frequent_words(text):
# Tokenize the text into words
    words = word_tokenize(text)
# Filter out stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
# Calculate the frequency distribution of words
    freq_dist = FreqDist(filtered_words)
# Get the 50 most frequent words
    most_frequent = freq_dist.most_common(50)
    return most_frequent
# Example usage:
sample_text = "This is an example text. It contains some words, and some of these words may repeat. This is just an example."
result = most_frequent_words(sample_text)
# Display the result
print("50 most frequent words (excluding stopwords):")
print(result)
