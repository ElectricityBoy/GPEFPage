import streamlit as st
from multiapp import MultiApp
from apps import home, data 

app = MultiApp()

st.set_page_config(
            page_title="GPEF",
            layout="wide",
        )

# Add all your application here
app.add_app("Pagina Inicial", home.app)
app.add_app("Analise dos Dados", data.app)


# The main app
app.run()
