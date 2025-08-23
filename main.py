from sentiment.preprocessing import clean_text
from sentiment.model import build_model
from sentiment.evalution import evaluate

import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    # Load dataset
    df = pd.read_csv("data/tweets.csv")  # Assume a CSV with 'text' and 'label' columns
    df['cleaned'] = df['tweet'].apply(clean_text)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(df['cleaned'], df['label'], test_size=0.2, random_state=42)

    # Build model
    vectorizer, model = build_model()
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train
    model.fit(X_train_vec, y_train)

    # Predict
    y_pred = model.predict(X_test_vec)

    # Evaluate
    evaluate(y_test, y_pred)

if __name__ == "__main__":
    main()
