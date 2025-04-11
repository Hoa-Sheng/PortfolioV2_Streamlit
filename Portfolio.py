import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Configuration de la page
st.set_page_config(page_title="Portfolio", page_icon=":briefcase:", layout="wide")

# Titre principal
st.title("Bienvenue sur mon Portfolio")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Accueil", "À propos", "Projets", "Contact"])

# Page d'accueil
if page == "Accueil":
    st.header("Accueil")
    st.write("Bienvenue sur mon portfolio. Explorez mes projets, apprenez-en plus sur moi et contactez-moi !")

# Page À propos
elif page == "À propos":
    st.header("À propos de moi")
    st.write("""
    Bonjour, je suis [Votre Nom], un développeur passionné par la création de solutions innovantes.
    J'ai de l'expérience dans [vos compétences principales] et je suis toujours à la recherche de nouveaux défis.
    """)

# Page Projets
elif page == "Projets":
    st.header("Mes Projets")
    st.write("Voici quelques-uns de mes projets récents :")
    projets = st.selectbox("Sélectionnez un projet", ["Projet 1", "Projet 2", "Projet 3"])
    if projets == "Projet 1":
        st.write("Description du Projet 1")
        st.image("image_projet_1.jpg", caption="Image du Projet 1")
    elif projets == "Projet 2":
        st.write("Description du Projet 2")
        st.image("image_projet_2.jpg", caption="Image du Projet 2")
    elif projets == "Projet 3":
        st.write("Description du Projet 3")
        st.image("image_projet_3.jpg", caption="Image du Projet 3")

# Page Contact
elif page == "Contact":
    st.header("Contactez-moi")
    st.write("Vous pouvez me contacter via les moyens suivants :")
    st.write("- 📧 **Email** : cong.hoa@yahoo.com")
    st.write("- 🔗 **LinkedIn** : [![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hoa-sheng-cong-8b66a5251/)")
    st.write("- 🐙 **GitHub** : [![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github&logoColor=white)](https://github.com/Hoa-Sheng)")

# Pied de page
st.sidebar.write("---")
st.sidebar.write("Portfolio créé avec ❤️ en utilisant Streamlit.")