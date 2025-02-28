import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_auc_score
from xgboost import XGBClassifier


if (__name__ == "__main__") : 

    X = df.drop(columns = ["target"])
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    xgb_model = XGBClassifier(
    n_estimators = 200, 
    max_depth = 6, 
    learning_rate = 0.1, 
    eval_metric = "logloss",
    reg_lambda = 10,
    reg_alpha = 2,
    random_state = 42
    )

    xgb_model.fit(X_train, y_train)

    test_file_path = "./data/test.csv" # setting
    
    df = pd.read_csv(test_file_path)
    
    test_ids = df["ID"]
    X_test = df

    y_pred_proba = xgb_model.predict_proba(X_test)[:, 1]

    submission = pd.DataFrame({"ID": test_ids, "probability": y_pred_proba})
    submission.to_csv("submission.csv", index = False)
