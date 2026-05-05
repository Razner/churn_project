from sklearn.metrics import accuracy_score

def evaluate(model, X_test, y_test):
    # Le modèle fait des prédictions sur les données de test
    preds = model.predict(X_test)
    
    # On calcule le taux de bonnes prédictions
    acc = accuracy_score(y_test, preds)

    print("Accuracy:", acc)