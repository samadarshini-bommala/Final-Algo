from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import r2_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression, make_classification
import pandas as pd

# --------- Linear Regression ----------
def train_linear_regression():
    # Generate dummy data for regression
    X, y = make_regression(n_samples=100, n_features=2, noise=10.0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    score = r2_score(y_test, predictions)

    return {
        "model_type": "linear_regression",
        "r2_score": score,
        "coefficients": model.coef_.tolist(),
        "intercept": model.intercept_
    }

# --------- Logistic Regression ----------
def train_logistic_regression():
    # Generate dummy data for classification
    X, y = make_classification(n_samples=100, n_features=2, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    report = classification_report(y_test, predictions, output_dict=True)

    return {
        "model_type": "logistic_regression",
        "classification_report": report
    }

