from collections import Counter

text = "NLP is fun and NLP is easy to learn"

# Tokenize words
words = text.lower().split()

# Count frequency
freq = Counter(words)

print("Word Frequency:")
for word, count in freq.items():
    print(word, ":", count)
