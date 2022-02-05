from faulthandler import is_enabled
import pandas as pd
import datetime
import streamlit as st
from PIL import Image


def analise(dfs):
    df = pd.read_csv(dfs)
    columns = ['Unnamed: 0','TP_CATEGORIA_ADMINISTRATIVA','TP_NIVEL_ACADEMICO','CO_UF_NASCIMENTO' ]
    df.drop(columns, inplace=True, axis=1)
    df = df.rename(columns = {'NU_ANO_CENSO': 'Ano do senso', 'TP_TURNO':'Turmo','TP_COR_RACA':'Raça','TP_SEXO':'Sexo','NU_IDADE':'Idade','TP_SITUACAO':'Situação','NU_ANO_INGRESSO':'Ano de Ingresso','TP_ESCOLA_CONCLUSAO_ENS_MEDIO':'Escola de Conclusão do Ensino Médio','IN_CONCLUINTE':'Concluinte','NU_ANO_INGRESSO':'Ano de Ingresso','IN_RESERVA_VAGAS':'Reserva de Vagas','IN_APOIO_SOCIAL':'Apoio Social','IN_DEFICIENCIA': 'Deficiência'}, inplace = False)
    df['Raça'] = df['Raça'].replace({0: 'Não declarou', 1: 'Branca',2: 'Preta', 3: 'Parda', 9: 'Não informado',4: 'Amarelo', 5: 'Indígena'})
    df['Escola de Conclusão do Ensino Médio'] = df['Escola de Conclusão do Ensino Médio'].replace({ 1: 'Pública', 2: 'Privada',
              9: 'Não informado'})
    df['Apoio Social'] = df['Apoio Social'].replace({ 0: 'Não', 1 : 'Sim' })
    df['Situação'] = df['Situação'].replace({ 2: 'Cursando', 3: 'Trancamento', 4: 'Desviculado', 5: 'Transferido', 6: 'Formado',7: 'Falecido'})
    df['Sexo']= df['Sexo'].replace({1: 'Mulher',2:'Homem'})
    df['Concluinte'] = df['Concluinte'].replace({ 0: 'Não', 1 : 'Sim' })
    df.reset_index(drop=True, inplace=True)

    return df


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

    st.title('Análise dos dados ', datetime.date)
  
    #Sidebar
    regions = {'Nordeste': 'REGIAO_NORDESTE_.csv','Norte': 'REGIAO_NORTE_.csv', 'Sudeste': 'REGIAO_SUDESTE_.csv', 'Sul': 'REGIAO_SUL_.csv','Centro Oeste': 'REGIAO_CO_.csv'}

    option = st.sidebar.selectbox('Escolha o ano do Senso:', (2018,2019))
    menu = st.sidebar.radio("Selecione uma região: ",regions.keys())


    
   #Dataframe
   
    df = analise(regions.get(menu))
    
   
    st.write("---")
    st.write("""Os resultados a seguir foram captados a partir do Senso de Educação do Ensino Superior do Brasil do ano de """,option, """disponilizado pelo INEP. 
    Foi realizado um tratamento dos dados utilizando a linguagem de programação Python para a análise dos estudantes dos cursos de Engenharia de todo o Brasil.
    """ )
    st.write("---")
    st.header(menu)
    st.dataframe(df.loc[df['Ano do senso'] == option])
    st.write("---")

    #Valores
    sexos = df.Sexo.value_counts()
    st.write("""Na região """,menu, " foi registrado um total de ", sexos["Mulher"], " estudantes mulheres e ",sexos["Homem"]," estudantes homens com os seguintes abaixo.")
