import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('😁 zBOT96 on Action!')

st.info('My First Streamlit App, so far so good...')

with st.expander('Data'):
  st.write('**Raw Data (dataframe)**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/penguins_cleaned.csv')
  df

  st.write('X data')
  X_raw=df.drop('species',axis=1)
  X_raw

  st.write('y data') 
  y_raw=df.species
  y_raw

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
  
input_penguins = pd.concat([input_df,X_raw],axis=0)

with st.expander('Input features'):
  st.write('**Input penguin data**')
  input_df
  st.write('**Combined penguin data**')
  input_penguins

# Encode X_raw
encode = ['island','sex']
df_penguins = pd.get_dummies(input_penguins,prefix=encode)
input_row = df_penguins[:1]
X=df_penguins[1:]

# Encode y_raw
target_mapper = {'Adelie': 0,'Chinstrap': 1,'Gentoo': 2}
target_encode = lambda x : target_mapper[x]
y=y_raw.apply(target_encode)

with st.expander('Data preparation'):
  st.write('**Encoded Input Penguin (X)**')
  input_row
  st.write('**Encoded y**')
  y

# Model training and inference
## Training the model
clf = RandomForestClassifier()
clf.fit(X,y)

# Prediction
prediction = clf.predict(input_row)
prediction_proba = clf.predict_proba(input_row)
prediction_proba
prediction




  


