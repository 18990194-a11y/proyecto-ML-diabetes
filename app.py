import streamlit as st
import numpy as np
import joblib

modelo = joblib.load("modelo_logistic.pkl")

st.title("Predicción de Diabetes")

st.write("Nombre: Rosa Maria Flores Echeverria")
st.write("Código ISIL: 18990194")
st.markdown("[Ver Cuaderno de Google Colab (Modo Lector)](https://colab.research.google.com/drive/1JdT-Hm3E-ZHROKLC3wKCUxr3-h3Gs2f7?usp=sharing)")

pregnancies = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
bloodpressure = st.number_input("BloodPressure")
skinthickness = st.number_input("SkinThickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("DiabetesPedigreeFunction")
age = st.number_input("Age")

if st.button("Predecir"):

    datos = np.array([[pregnancies,
                       glucose,
                       bloodpressure,
                       skinthickness,
                       insulin,
                       bmi,
                       dpf,
                       age]])

    prediccion = modelo.predict(datos)

    if prediccion[0] == 1:
        st.error("El paciente podría tener diabetes")
    else:
        st.success("El paciente no tendría diabetes")


