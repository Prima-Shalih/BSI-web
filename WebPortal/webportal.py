import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('WebPortal1.sav','rb'))

df = pd.read_excel("WebPortalCoba.xlsx")
df['TANGGAL'] = pd.to_datetime(df['TANGGAL'], format='%D')
df.set_index(['TANGGAL'], inplace=True)

st.title('Forecasting Web Portal')
year = st.slider("Tentukan Hari",1,21, step=1)

pred = model.forecast(year)
pred = pd.DataFrame(pred, columns=['WEB PORTAL'])

if st.button("Predict"):

    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig, ax = plt.subplots()
        df['WEB PORTAL'].plot(style='--', color='gray', legend=True, label='known')
        pred['WEB PORTAL'].plot(color='b', legend=True, label='Prediction')
        st.pyplot(fig)