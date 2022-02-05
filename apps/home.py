import pandas as pd
import datetime
import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

#Streamlite configurations


#----------------------
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()


# Load assets

animation = load_lottieurl("https://assets1.lottiefiles.com/private_files/lf30_lps8ojuw.json")
image1 = Image.open('images/congresso75anos.png')
image3 = Image.open("images/crtigo1.png")
image2 = Image.open('images/congresso2021.png')


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

    with st.container():
      st.write("---")
      left_column, right_column = st.columns(2)
      with left_column:
        st.header('Quem somos?')
        st.write("##")
        st.markdown('<p align="justify"> A atividade consiste em desenvolver no Programa de Educação Tutorial um Grupo de Pesquisa para tratar de questões de gênero, a fim de diagnosticar, por exemplo, as causas da baixa participação de mulheres nas áreas de ciências exatas e engenharias - inclusive no PET Elétrica. Além de desenvolver pesquisas, a atividade tem o propósito de gerar um arcabouço teórico com objetivo de fundamentar outras atividades, de preferência de cunho extensionista, com intuito de garantir equidade de gênero. Além disso, pretende-se promover debates e discussões acerca das questões estudadas e gerar resultados como a escrita de artigos. </p>', unsafe_allow_html=True)

        st.write("[Vídeo Apresentação >](https://www.youtube.com/watch?v=tBsMCZTv32k)")


      with right_column:
        st_lottie(animation, height = 300, key = "coding")

    #Videos públicados

    with st.container():
      st.write("---")
      st.header("Vídeos Publicados")
      st.write("##")

      image_column, text_column = st.columns((1,2))

      with image_column:
        #insert image
        st.image(image1)
      with text_column:
        st.subheader("A Evasão Feminina no Curso de Engenharia Elétrica")
        st.write(
          """
          Este trabalho visa realizar um estudo de caso dentro da Universidade Federal da Bahia (UFBA) voltado à evasão feminina do curso de Engenharia Elétrica. Assim, foram analisados os  Microdados do Censo da Educação Superior entre os anos de 2009 e 2017, os quais foram obtidos do INEP (Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira). Para isso, fez-se uso das linguagens de programação Python e R com enfoque nas seguintes variáveis: escola de conclusão do Ensino Médio, raça e idade. 
          Congresso UFBA 75 Anos
        """)

        st.markdown("[Assista o vídeo](https://www.youtube.com/watch?v=LJjQ1lI0GYM)")

      with image_column:
        #insert image
        st.image(image2)
      with text_column:
        st.subheader("Grupo de Pesquisa em Empoderamento Feminino")
        st.write(
          """
          Este vídeo tem como objetivo apresentar o Grupo de Pesquisa em Empoderamento Feminino (GPEF), uma atividade desenvolvida pelo Programa de Educação Tutorial do Curso de Engenharia Elétrica da Universidade Federal da Bahia (PET Elétrica UFBA), além de mostrar a discrepância que é possível observar entre quantidade de homens e de mulheres presentes nas áreas de Ciências Exatas e Engenharias, com foco no curso de Engenharia Elétrica da UFBA.
          Congresso UFBA 2021
        """)

        st.markdown("[Assista o vídeo](https://www.youtube.com/watch?v=tBsMCZTv32k)")
      
    #Produções

    with st.container():
      st.write("---")
      st.header("Artigos publicados")
      st.write("##")

      image_column, text_column = st.columns((1,2))

      with image_column:
        #insert image
        st.image(image3)
      with text_column:
        st.markdown("#### Uma iniciativa do programa de educação tutorial de engenharia elétrica da Universidade Federal da Bahia ")
        st.write(
          """
          Brazilian Journal of Development
          -  Nathane Lima Cintra
          -  Moira Bastos Prates
          -  Mariana de Carmo Nascimento
          -  Beatriz Cerqueira Brandão de Jesus
          -  Isaac Pereira da Conceição Araújo
        """)

        st.markdown("[Acesse o artigo](https://brazilianjournals.com/index.php/BRJD/article/view/27915/22095)")
  







    












