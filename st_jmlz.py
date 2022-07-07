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

# Pie chart, where the slices will be ordered and plotted counter-clockwise:

#The plot
SJR_Q = DATA.SJR_Q.value_counts()

fig = go.Figure(
    go.Pie(
    labels = SJR_Q.index,
    values = SJR_Q.values,
    hoverinfo = "label+percent",
    textinfo = "value"
))

st.header("SJR_Q Scimago ranking")
st.plotly_chart(fig)


