import pickle
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

model = pickle.load(open('Model_Prediksi.sav','rb'))

df = pd.read_csv("WindSpeed.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
df.set_index(['Date'], inplace=True)

st.title('Peramalan Kecepatan Angin')
date = st.slider("Prediksi berapa hari kedepan",1,100, step=1)

pred = model.forecast(date)
pred = pd.DataFrame(pred, columns=['Wind Speed_km/h'])

if st.button("Prediksi"):
    col1, col2 = st.columns([2,3])
    with col1:
        st.dataframe(pred)
    with col2:
        fig,ax = plt.subplots()
        df['Wind Speed_km/h'].plot(style='--', color='gray', legend=True, label='known')
        pred['Wind Speed_km/h'].plot(color='b', legend=True, label='prediction')
        st.pyplot(fig)