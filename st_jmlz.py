import streamlit as st
import pandas as pd
from streamlit.hello import Hello
import numpy as np
import plotly.graph_objects as go

st.title('3BIO - JMLZ Dashboard')

DATA = pd.read_csv('/Users/jmlz_rp/Documents/BIOS/streamlit_jmlz/Informe seleccion de metricas/articulos.CSV')

st.write( """ 
# Gruplac Publindex Metrics
Personal work for 3BIO proyect by jmlz 
""" )

categoria           = DATA.categoria_revista.value_counts(ascending=False)
categoria_articulos = DATA.SJR_Q.str.replace('-','Sin categoria').value_counts(ascending=False)

# Pie chart :: Scimago Ranking
SJR_Q = DATA.SJR_Q.value_counts()

fig = go.Figure(
    go.Pie(
    labels=SJR_Q.index, 
    hole=0.3,
    values = SJR_Q.values
))

st.header("Pie chart")
st.plotly_chart(fig)


