import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

# Simple dummy data
def load_sample_data(task="regression"):
    # For regression: predict price
    # For classification: binarize price
    data = pd.DataFrame({
        "area": [750, 800, 850, 900, 950, 1000],
        "rooms": [2, 2, 3, 3, 4, 4],
        "price": [150, 160, 170, 180, 200, 220]
    })
    if task == "classification":
        data["price"] = (data["price"] > 175).astype(int)
    return data

def train_model(model_type="regression"):
    df = load_sample_data(task=model_type)
    X = df[["area", "rooms"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    if model_type == "regression":
        model = LinearRegression()
    else:
        model = LogisticRegression()

    model.fit(X_train, y_train)
    return model, X_test, y_test
