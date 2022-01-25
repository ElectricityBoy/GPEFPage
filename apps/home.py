from faulthandler import is_enabled
import pandas as pd
import datetime
import streamlit as st
import plotly.express as px
from PIL import Image

#Streamlite configurations


def app():
    



  
    #Functions


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
    st.subheader('PET ELÉTRICA UFBA')

    

    st.markdown('<p align="justify"> A atividade consiste em desenvolver no PET um Grupo de Pesquisa para tratar de questões de gênero, a fim de diagnosticar, por exemplo, as causas da baixa participação de mulheres nas áreas de ciências exatas e engenharias - inclusive no PET Elétrica. Além de desenvolver pesquisas, a atividade tem o propósito de gerar um arcabouço teórico com objetivo de fundamentar outras atividades, de preferência de cunho extensionista, com intuito de garantir equidade de gênero. Além disso, pretende-se promover debates e discussões acerca das questões estudadas e gerar resultados como a escrita de artigos. </p>', unsafe_allow_html=True)

    imagem = Image.open('logo.png')
    st.image(imagem)












