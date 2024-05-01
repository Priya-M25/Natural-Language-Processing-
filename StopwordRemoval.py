from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sent = """This is a sample sentence,
                showing off the stop words filtration."""
stop_words = set(stopwords.words('english'))
print(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
#with no lower case conversion
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
print("Output Follows")
print("Original Text:",word_tokens)
print("Filtered Sentence:",filtered_sentence)
