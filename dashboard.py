import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Nettoyage simple
df["Churn"] = df["Churn"].str.strip()

st.title("Dashboard Churn - Analyse Clients")

# Menu
page = st.sidebar.selectbox(
    "Choisir une section",
    [
        "Vue générale",
        "Clients à risque",
        "Analyse contrats",
        "Analyse âge",
        "Analyse services",
        "Analyse support",
        "Actions pour réduire le churn"   # <-- AJOUT
    ]
)

if page == "Vue générale":

    st.header("Vue générale")

    st.write(df.head())

    churn_rate = (df["Churn"] == "Yes").mean()

    st.metric("Taux de churn (%)", round(churn_rate * 100, 2))
    st.metric("Nombre de clients", len(df))
    st.metric("Clients qui partent", (df["Churn"] == "Yes").sum())

    st.subheader("Churn par type de contrat")
    st.bar_chart(df.groupby("Contract")["Churn"].apply(lambda x: (x == "Yes").mean()))

    st.subheader("Charges vs ancienneté")

    fig, ax = plt.subplots()

    ax.scatter(
        df[df["Churn"] == "No"]["tenure"],
        df[df["Churn"] == "No"]["MonthlyCharges"],
        color="green",
        alpha=0.6,
        label="No Churn"
    )

    ax.scatter(
        df[df["Churn"] == "Yes"]["tenure"],
        df[df["Churn"] == "Yes"]["MonthlyCharges"],
        color="red",
        alpha=0.6,
        label="Churn"
    )

    ax.set_xlabel("Ancienneté (tenure)")
    ax.set_ylabel("Charges mensuelles")
    ax.set_title("Relation charges / ancienneté")
    ax.legend()

    st.pyplot(fig)

elif page == "Clients à risque":

    st.header("Clients à risque")

    risk_df = df[df["Churn"] == "Yes"]

    st.dataframe(risk_df.head())

    st.write(risk_df[["tenure", "MonthlyCharges"]].mean())

elif page == "Analyse contrats":

    st.header("Analyse des contrats")

    churn_by_contract = df.groupby("Contract")["Churn"].apply(lambda x: (x == "Yes").mean())

    st.bar_chart(churn_by_contract)

elif page == "Analyse âge":

    st.header("Analyse par âge / Senior Citizen")

    churn_by_senior = df.groupby("SeniorCitizen")["Churn"].apply(lambda x: (x == "Yes").mean())

    st.bar_chart(churn_by_senior)

    st.write("0 = non senior, 1 = senior")

elif page == "Analyse services":

    st.header("Analyse des services")

    # Internet service
    st.subheader("Churn par type Internet")
    churn_by_internet = df.groupby("InternetService")["Churn"].apply(lambda x: (x == "Yes").mean())
    st.bar_chart(churn_by_internet)

    # Fibre optique vs autre
    st.subheader("Fibre optique vs autres")
    fiber_df = df.copy()
    fiber_df["Fiber"] = fiber_df["InternetService"] == "Fiber optic"

    st.bar_chart(fiber_df.groupby("Fiber")["Churn"].apply(lambda x: (x == "Yes").mean()))

elif page == "Analyse support":

    st.header("Niveau de support client")

    churn_by_support = df.groupby("TechSupport")["Churn"].apply(lambda x: (x == "Yes").mean())

    st.bar_chart(churn_by_support)

    st.write("Yes = support technique, No = pas de support")

elif page == "Actions pour réduire le churn":   # <-- NOUVELLE SECTION

    st.header("Actions pour réduire le churn")

    actions_df = pd.DataFrame({
        "Facteur identifié": [
            "Contrats Month-to-Month",
            "Faible ancienneté (tenure)",
            "Clients seniors",
            "Fibre optique",
            "Absence de support technique",
            "Charges mensuelles élevées",
        ],
        "Constat": [
            "Churn très élevé",
            "Les clients récents churnent le plus",
            "Churn plus élevé chez les seniors",
            "Churn le plus élevé parmi les types Internet",
            "Churn très élevé sans support",
            "Sensibilité au prix",
        ],
        "Action recommandée": [
            "Inciter à passer sur 12/24 mois (réductions, avantages)",
            "Onboarding renforcé : appel de bienvenue, offres personnalisées",
            "Assistance dédiée, simplification de l'expérience",
            "Améliorer qualité fibre : diagnostic, interventions rapides, dédommagements",
            "Support minimum gratuit, automatisation du support",
            "Offres personnalisées, remises temporaires",
        ]
    })

    st.dataframe(actions_df)
