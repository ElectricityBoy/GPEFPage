from faulthandler import is_enabled
import pandas as pd
import datetime
import streamlit as st
import plotly.express as px
from PIL import Image



def app():




    #NavegationBar
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #283566;">
    <a class="navbar-brand" href="" target="_blank">GPEF</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
        <li class="nav-item">
            <a class="nav-link" disabled href="https://peteletricaufba.github.io" target="_blank">Site do PET</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://www.instagram.com/peteletricaufba/" target="_blank">Instagram</a>
        </li>
        </ul>
    </div>
    </nav>
    """, unsafe_allow_html=True)

    st.title('GPEF - GRUPO DE PESQUISA EM EMPODERAMENTO FEMININO ', datetime.date)
  
    #Sidebar
    regions = {'Nordeste': 'REGIAO_NORDESTE_.csv','Norte': 'REGIAO_NORTE_.csv', 'Sudeste': 'REGIAO_SUDESTE_.csv', 'Sul': 'REGIAO_SUL_.csv','Centro Oeste': 'REGIAO_CO_.csv'}

    option = st.sidebar.selectbox('Escolha o ano do Senso:', (2018,2019))
    menu = st.sidebar.radio("Selecione uma região: ",regions.keys())





    df = pd.read_csv(regions.get(menu),encoding='unicode_escape')
    #Dataframe
    st.header(menu)
    st.dataframe(df.loc[df.NU_ANO_CENSO == option])