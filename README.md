# Projet Churn - Machine Learning

---

## Structure du projet
- main.py → lance tout le pipeline ML
- src/ → code du modèle (data, preprocessing, train, evaluation)
- model/ → modèle sauvegardé
- app.py → API FastAPI
- dashboard.py → dashboard Streamlit
- data/ → dataset

---

## Installation

> Installer les dépendances :

- pip install -r requirements.txt

> Lancer le projet Machine Learning :

- python main.py

> Lancer l’API

- uvicorn app:app --reload

> Lancer le Dashboard

- streamlit run dashboard.py