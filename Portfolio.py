import streamlit as st
import streamlit.components.v1 as components
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
    st.markdown("""<h2>Accueil</h2>""", unsafe_allow_html=True)
    st.write("Bienvenue sur mon portfolio. Explorez mes projets, apprenez-en plus sur moi et contactez-moi !")
    st.markdown("""<h2>Mes compétences</h2>""", unsafe_allow_html=True)
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; align-items: center; margin-top: 20px;">
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg" alt="Jupyter" style="width: 120px; height: auto;">
            <p>Jupyter</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-learn" style="width: 120px; height: auto;">
            <p>Scikit-learn</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Pandas_mark.svg" alt="Pandas" style="width: 120px; height: auto;">
            <p>Pandas</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" alt="NumPy" style="width: 120px; height: auto;">
            <p>NumPy</p>
        </div>
        <div style="text-align: center;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="Matplotlib" style="width: 120px; height: auto;">
            <p>Matplotlib</p>
        </div>
        <div style="text-align: center;">
            <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="Seaborn" style="width: 120px; height: auto;">
            <p>Seaborn</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""<h2>Mon parcours</h2>""", unsafe_allow_html=True)
    components.html("""
    <section style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; padding: 50px 0; font-family: 'Jost', sans-serif;">
        <div style="width: 80%; max-width: 800px; margin: 0 auto; display: grid; grid-template-columns: 1fr 3px 1fr; align-items: center;">

            <!-- Événement 1 -->
            <div style="text-align: right; padding: 10px; background-color: #f0f0f0; border-radius: 10px;">
                <h3 style="margin: 0; font-size: 1.2rem;">2025</h3>
                <p style="margin: 5px 0;">Développeur Full Stack</p>
                <p style="margin: 0;">Travail sur des projets innovants en utilisant Python, React et Node.js.</p>
            </div>
            <div style="position: relative; background: #E94057; width: 3px; height: 100%;"></div>
            <div></div>

            <!-- Événement 2 -->
            <div></div>
            <div style="position: relative; background: #E94057; width: 3px; height: 100%; "></div>
            <div style="text-align: left; padding: 10px; background-color: #f0f0f0; border-radius: 10px;">
                <h3 style="margin: 0; font-size: 1.2rem;">2023</h3>
                <p style="margin: 5px 0;">Stage en Data Science</p>
                <p style="margin: 0;">Analyse de données et création de modèles prédictifs avec Python et Scikit-learn.</p>
            </div>

            <!-- Événement 3 -->
            <div style="text-align: right; padding: 10px; background-color: #f0f0f0; border-radius: 10px;">
                <h3 style="margin: 0; font-size: 1.2rem;">2020</h3>
                <p style="margin: 5px 0;">Diplôme en Informatique</p>
                <p style="margin: 0;">Obtention d'un diplôme en informatique avec spécialisation en développement logiciel.</p>
            </div>
            <div style="position: relative; background: #E94057; width: 3px; height: 100%;"></div>
            <div></div>

        </div>
    </section>
    """, height=600)

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