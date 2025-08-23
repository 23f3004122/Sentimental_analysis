import re
import nltk
from nltk.corpus import stopwords

def clean_text(text):
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower().split()
    text = [word for word in text if word not in stopwords.words('english')]
    return " ".join(text)
