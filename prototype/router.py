"""Step 1 — the router (rung 2: classical ML). TF-IDF + logistic regression on data/tickets_synthetic.csv."""
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

MODEL = None
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def train(csv_path=None):
    """Train on text -> category (how_do_i | pay_legal | billing | product). Never reads evals/."""
    global MODEL
    df = pd.read_csv(csv_path or os.path.join(ROOT, "data", "tickets_synthetic.csv"))
    MODEL = make_pipeline(TfidfVectorizer(ngram_range=(1, 2), min_df=1, sublinear_tf=True),
                          LogisticRegression(max_iter=2000, C=10))
    MODEL.fit(df["text"], df["category"])
    return MODEL


def predict(text):
    """Return (category, confidence). Confidence = max predict_proba."""
    if MODEL is None:
        train()
    proba = MODEL.predict_proba([text])[0]
    i = proba.argmax()
    return MODEL.classes_[i], float(proba[i])
