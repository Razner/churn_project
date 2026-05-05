import pandas as pd

def preprocess(df):
    # On enlève les espaces dans les noms de colonnes
    df.columns = df.columns.str.strip()
    # On supprime les lignes avec des valeurs manquantes
    df = df.dropna()

    # Transformer churn en 0/1
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df