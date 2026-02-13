from nltk.util import ngrams
from nltk.tokenize import word_tokenize

text = "Natural language processing is fun"

tokens = word_tokenize(text)

# Bigrams
bigrams = list(ngrams(tokens, 2))

# Trigrams
trigrams = list(ngrams(tokens, 3))

print("Bigrams:", bigrams)
print("Trigrams:", trigrams)
