
import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk import bigrams

# Download NLTK resources (stopwords)
nltk.download('stopwords')

def get_frequent_bigrams(text, N=50):
# Tokenize the text into words
words = nltk.word_tokenize(text)

# Create a list of English stopwords
stop_words = set(stopwords.words('english'))

# Filter out stopwords and create bigrams
filtered_bigrams = [bigram for bigram in bigrams(words) if all(word.lower() not in stop_words for word in bigram)]

# Calculate the frequency distribution of bigrams
freq_dist = FreqDist(filtered_bigrams)

# Get the N most common bigrams
most_common_bigrams = freq_dist.most_common(N)
return most_common_bigrams

# Example text
example_text = """
Lakshadweep, the group of 36 islands is known for its exotic and sun-kissed beaches and lush green landscape. The name Lakshadweep in Malayalam and Sanskrit means ‘a hundred thousand islands’. India’s smallest Union Territory Lakshadweep is an archipelago consisting of 36 islands with an area of 32 sq km. It is a uni-district Union Territory and comprises of 12 atolls, three reefs, five submerged banks and ten inhabited islands. The islands have a total area of 32 sq km. The capital is Kavaratti and it is also the principal town of the UT. All Islands are 220 to 440 km away from the coastal city of Kochi in Kerala, in the emerald Arabian Sea. he natural landscapes, the sandy beaches, abundance of flora and fauna and the absence of a rushed lifestyle enhance the mystique of Lakshadweep.
"""

# Call the function and print the 50 most frequent bigrams omitting stopwords
result = get_frequent_bigrams(example_text, N=50)
for bigram, frequency in result:
print(bigram, frequency)
