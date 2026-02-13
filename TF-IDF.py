from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "NLP is interesting",
    "NLP is useful",
    "I love learning NLP"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

print("Words:", vectorizer.get_feature_names_out())
print("TF-IDF Matrix:\n", tfidf_matrix.toarray())
