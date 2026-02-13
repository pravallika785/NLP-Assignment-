import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "NLP makes computers understand human language"

tokens = word_tokenize(text)

tags = pos_tag(tokens)

print("POS Tags:")
for word, tag in tags:
    print(word, ":", tag)
