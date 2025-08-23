This project performs sentiment analysis on text data to classify whether a piece of text expresses a positive or negative sentiment.

It was first implemented in Jupyter Notebook and later modularized into Python files for easier development and reuse in VS Code.

Project structure

sentimental_analysis/
│── data/                  # Datasets (CSV or text files)
│── notebook/              # Original Jupyter notebooks
│── sentiment/             # Main Python package
│   │── __init__.py
│   │── preprocessing.py   # Text cleaning & preprocessing
│   │── model.py           # Model creation and training
│   │── evaluation.py      # Model evaluation metrics
│   │── utils.py           # Helper functions
│── main.py                # Entry point to run the project
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│── venv/                  # Virtual environment (not pushed to git)
