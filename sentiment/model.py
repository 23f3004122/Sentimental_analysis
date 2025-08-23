from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def build_model():
    vectorizer = CountVectorizer(max_features=5000)
    model = MultinomialNB()
    return vectorizer, model
