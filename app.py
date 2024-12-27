import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title("Mini Application Streamlit")

# Description
st.write("""
### Cette application affiche un tableau de données et un graphique interactif.
""")

# Génération de données aléatoires
data = pd.DataFrame({
    'X': np.random.randint(0, 100, 50),
    'Y': np.random.randint(0, 100, 50)
})

# Affichage du tableau
st.write("Voici un tableau de données généré aléatoirement :")
st.dataframe(data)

# Affichage d'un graphique interactif
st.write("Voici un graphique des données :")
st.line_chart(data)

# Slider interactif
val = st.slider("Filtrer les données où X est inférieur à", 0, 100, 50)
filtered_data = data[data['X'] < val]
st.write("Données filtrées :")
st.dataframe(filtered_data)
