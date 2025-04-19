import numpy as np
from sklearn.metrics import r2_score, accuracy_score
from scipy import stats

def evaluate_model(model, X_test, y_test, model_type="regression"):
    y_pred = model.predict(X_test)
    result = {}

    if model_type == "regression":
        result["r2_score"] = r2_score(y_test, y_pred)
        result["coefficients"] = model.coef_.tolist()
        result["intercept"] = model.intercept_

        # Basic t-stat approximation
        X = X_test.to_numpy()
        residuals = y_test - y_pred
        dof = len(X) - len(model.coef_)
        mse = np.mean(residuals**2)
        var_b = mse * (np.linalg.inv(X.T @ X).diagonal())
        std_b = np.sqrt(var_b)
        t_stats = model.coef_ / std_b
        result["t_statistics"] = t_stats.tolist()

    else:
        result["accuracy"] = accuracy_score(y_test, y_pred)

    return result
