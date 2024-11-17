import streamlit as st
import pandas as pd

st.title('😁 zBOT96 on Action!')

st.info('My First Streamlit App, so far so good...')

with st.expander('Data'):
  st.write('**Raw Data (dataframe)**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

st.write('X data')
X=df.drop('species',axis=1)
X

st.write('y data') 
y=df.species
y


