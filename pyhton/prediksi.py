import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('Prediksi_PengenalanWajah2.sav','rb'))

df = pd.read_excel("Pengenalan Wajah.xlsx")
df['Tanggal'] = pd.to_datetime(df['Tanggal'], format='%Y')
df.set_index(['Tanggal'], inplace=True)

st.title('Forecasting Pengenalan Wajah')
year = st.slider("Tentukan Hari",1,78, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['Pengenalan Wajah'])

if st.button("Predict"):

    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['Pengenalan Wajah'].plot(style='--', color='gray', legend=True, label='known')
        pred['Pengenalan Wajah'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)