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
  bill_length_mm = st.slider('Bill length (mm)',32.1,59.6,43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1,21.5,17.2)
  flipper_length_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)',2700.00,6300.00,4207.00)

  data = {'island':island,
          'sex':gender,
          'bill_length_mm':bill_length_mm,
          'bill_depth_mm':bill_depth_mm,
          'flipper_length_mm':flipper_length_mm,
          'body_mass_g':body_mass_g
          }
  input_df= pd.DataFrame(data,index=[0])

input_penguins = pd.concat([input_df,X],axis=0)
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins,prefix=encode)
input_row = df_penguins[:1]

with st.expander('Input features'):
  st.write('**Input penguin data**')
  input_df
  st.write('**Combined penguin data**')
  input_penguins
  st.write('Encoded Input Penguin')
  input_row




  


