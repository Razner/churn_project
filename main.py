from src.data import load_data
from src.preprocessing import preprocess
from src.train import train_model
from src.evaluate import evaluate

def main():
    df = load_data("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    #On prépare les données (nettoyage + transformation)
    df = preprocess(df)

    #On entraîne le modèle
    model, X_test, y_test = train_model(df)

    #On évalue les performances
    evaluate(model, X_test, y_test)

if __name__ == "__main__":
    main()