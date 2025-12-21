# =========================================
# Fractal Analysis + ML Classification
# TMD vs Healthy Controls
# =========================================

import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

# ------------------------------
# Global Settings (Reproducibility)
# ------------------------------
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# ------------------------------
# Directory Setup
# ------------------------------
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "sample_data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# ------------------------------
# Load Data
# ------------------------------
DATA_PATH = os.path.join(DATA_DIR, "fractal_features.csv")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(
        "fractal_features.csv not found in sample_data/. "
        "Please add the synthetic dataset."
    )

df = pd.read_csv(DATA_PATH)

# ------------------------------
# Feature & Label Selection
# ------------------------------
X = df[["FD_right", "FD_left", "age", "gender"]]
y = df["label"]

# ------------------------------
# Train / Validation / Test Split
# 70% / 15% / 15%
# ------------------------------
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.30, random_state=RANDOM_SEED, stratify=y
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.50, random_state=RANDOM_SEED, stratify=y_temp
)

# ------------------------------
# Model Definitions + Hyperparameters
# ------------------------------
models = {
    "Logistic Regression": Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "model",
                LogisticRegression(
                    C=1.0, solver="lbfgs", max_iter=1000, random_state=RANDOM_SEED
                ),
            ),
        ]
    ),
    "Support Vector Machine": Pipeline(
        [
            ("scaler", StandardScaler()),
            (
                "model",
                SVC(
                    kernel="rbf",
                    C=1.0,
                    gamma="scale",
                    probability=True,
                    random_state=RANDOM_SEED,
                ),
            ),
        ]
    ),
    "K-Nearest Neighbors": Pipeline(
        [
            ("scaler", StandardScaler()),
            ("model", KNeighborsClassifier(n_neighbors=5, weights="distance")),
        ]
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=200, max_depth=None, min_samples_split=2, random_state=RANDOM_SEED
    ),
    "Gradient Boosting": GradientBoostingClassifier(
        n_estimators=150, learning_rate=0.05, max_depth=3, random_state=RANDOM_SEED
    ),
    "XGBoost": XGBClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=4,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric="logloss",
        random_state=RANDOM_SEED,
    ),
}

# ------------------------------
# Model Training & Evaluation
# ------------------------------
results = []

for name, model in models.items():
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    results.append(
        {
            "Model": name,
            "Accuracy": accuracy_score(y_test, y_pred),
            "Precision": precision_score(y_test, y_pred),
            "Recall": recall_score(y_test, y_pred),
            "F1-Score": f1_score(y_test, y_pred),
            "ROC AUC": roc_auc_score(y_test, y_prob),
        }
    )

# ------------------------------
# Save Results
# ------------------------------
results_df = pd.DataFrame(results)
results_path = os.path.join(RESULTS_DIR, "ML_performance_metrics.csv")
results_df.to_csv(results_path, index=False)

print("\n✅ ML analysis completed successfully!")
print(f"📁 Results saved to: {results_path}")
print(results_df)
