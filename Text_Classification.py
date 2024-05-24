import nltk
from nltk.corpus import movie_reviews
from nltk import FreqDist
from nltk import classify
from nltk import NaiveBayesClassifier

# Download the movie_reviews dataset if not already downloaded
nltk.download('movie_reviews')

# Feature extraction function
def extract_features(words):
    return dict(FreqDist(words))

# Prepare the dataset
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the documents
import random
random.shuffle(documents)

# Split the dataset into training and testing sets
split_ratio = int(len(documents) * 0.8)
train_set, test_set = documents[:split_ratio], documents[split_ratio:]

# Extract features using the defined function
training_features = [(extract_features(words), category) for (words, category) in train_set]
testing_features = [(extract_features(words), category) for (words, category) in test_set]

# Train the Naive Bayes classifier
classifier = NaiveBayesClassifier.train(training_features)

# Evaluate the classifier on the testing set
accuracy = classify.accuracy(classifier, testing_features)
print("Accuracy:", accuracy)

# Example sentences to classify
new_sentences = [
    "This movie was fantastic!",
    "I didn't like the plot of this film.",
    "The acting was superb in this movie.",
    "The screenplay was terrible."
]

# Classify the new sentences
for sentence in new_sentences:
    words = nltk.word_tokenize(sentence)
    features = extract_features(words)
    category = classifier.classify(features)
    print(f"Predicted category for '{sentence}': {category}")



''' 
Output:-

[nltk_data] Downloading package movie_reviews to /root/nltk_data...
[nltk_data]   Package movie_reviews is already up-to-date!

Accuracy: 0.7675

Predicted category for 'This movie was fantastic!': pos
Predicted category for 'I didn't like the plot of this film.': neg
Predicted category for 'The acting was superb in this movie.': pos
Predicted category for 'The screenplay was terrible.': neg

'''
