import streamlit as st
import pandas as pd
from streamlit.hello import Hello
import numpy as np
import matplotlib.pyplot as plt

st.title('3BIO - JMLZ Dashboard')

DATA = pd.read_csv('/Users/jmlz_rp/Documents/BIOS/streamlit_jmlz/Informe seleccion de metricas/articulos.CSV')

st.write( """ 
# Gruplac Publindex Metrics
Personal work for 3BIO proyect by jmlz 
""" )

categoria           = DATA.categoria_revista.value_counts(ascending=False)
categoria_articulos = DATA.SJR_Q.str.replace('-','Sin categoria').value_counts(ascending=False)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:

fig1, ax1 = plt.subplots()
SJR_Q = DATA.SJR_Q.value_counts()
ax1.pie(values=SJR_Q.values, names=SJR_Q.index, hole=0.3)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
