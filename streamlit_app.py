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

with st.expander('Data Visualisation'):
  # "bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g',color='species')

with st.sidebar:
  st.header('Input Features')
  island = st.selectbox('Island',('Torgersen','Biscoe','Dream'))
  gender = st.selectbox('Sex',('male','female'))
  bill_length_mm = st.slider('Bill Length (mm)',32.1,59.6,43.9)


