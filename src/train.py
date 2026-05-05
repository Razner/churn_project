from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib
import os
import pandas as pd

def train_model(df):

    # Variables
    categorical_cols = ["Contract", "InternetService"]
    numerical_cols = ["tenure", "MonthlyCharges"]

    X = df[categorical_cols + numerical_cols]
    y = df["Churn_Yes"] if "Churn_Yes" in df.columns else df["Churn"]

    # Preprocessing
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
            ("num", "passthrough", numerical_cols)
        ]
    )

    # Pipeline complet
    model = Pipeline(steps=[
        ("preprocessing", preprocessor),
        ("classifier", RandomForestClassifier(random_state=42))
    ])

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    # Save model
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/churn_pipeline.pkl")

    return model, X_test, y_test