import joblib
import streamlit as st
import time
import pandas as pd


model = joblib.load("model/knn.joblib")


st.set_page_config(page_title="BK Hungarian", page_icon=":pencil2:")

st.title("BK Hungarian")

  
col1, col2 = st.columns(2)
with col1:
  age = st.number_input(label="Age", min_value=0, max_value=100, value=0, step=1)
  st.markdown("<small>:orange[**Min**] value: :orange[**0**], :green[**Max**] value: :green[**100**]</small>", unsafe_allow_html=True)
with col2:
  sex = st.selectbox(label="Sex", options=["Male", "Female"])
  sex = 1 if sex == "Male" else 0

col3, col4 = st.columns(2)
with col3:
  cp = st.selectbox(label="Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
  cp = 1 if cp == "Atypical Angina" else 2 if cp == "Non-anginal Pain" else 3 if cp == "Asymptomatic" else 0
with col4:
  trestbps = st.number_input(label="Resting Blood Pressure", min_value=92.0, max_value=200.0, value=92.0, step=0.01)
  st.markdown("<small>:orange[**Min**] value: :orange[**92.0**], :green[**Max**] value: :green[**200.0**]</small>", unsafe_allow_html=True)

col5, col6 = st.columns(2)
with col5:
  chol = st.number_input(label="Serum Cholestoral (in mg/dl)", min_value=85.0, max_value=603.0, value=85.0, step=0.01)
  st.markdown("<small>:orange[**Min**] value: :orange[**85.0**], :green[**Max**] value: :green[**603.0**]</small>", unsafe_allow_html=True)
with col6:
  fbs = st.selectbox(label="Fasting Blood Sugar", options=["True", "False"])
  fbs = 1 if fbs == "True" else 0

col7, col8 = st.columns(2)
with col7:
  restecg = st.selectbox(label="Resting Electrocardiographic Results", options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
  restecg = 1 if restecg == "ST-T Wave Abnormality" else 2 if restecg == "Left Ventricular Hypertrophy" else 0
with col8:
  thalach = st.number_input(label="Maximum Heart Rate Achieved", min_value=82.0, max_value=190.0, value=82.0, step=0.01)
  st.markdown("<small>:orange[**Min**] value: :orange[**82.0**], :green[**Max**] value: :green[**190.0**]</small>", unsafe_allow_html=True)

col9, col10 = st.columns(2)
with col9:
  exang = st.selectbox(label="Exercise Induced Angina", options=["Yes", "No"])
  exang = 1 if exang == "Yes" else 0
with col10:
  oldpeak = st.number_input(label="ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=5.0, value=0.0, step=0.01)
  st.markdown("<small>:orange[**Min**] value: :orange[**0.0**], :green[**Max**] value: :green[**5.0**]</small>", unsafe_allow_html=True)

btn_predict = st.button(label="**Predict**", type="primary")

if btn_predict:
  inputs = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]]
  prediction = model.predict(inputs)[0]

  bar = st.progress(0)
  status_text = st.empty()

  for i in range(101):
    bar.progress(i)
    status_text.text(f"Predicting... {i}%")
    time.sleep(0.01)

    if i == 100:
      time.sleep(1)
      status_text.empty()
      bar.empty()
  
  if prediction == 0:
    st.balloons()
    st.success("You are healthy! :smile:")
  elif prediction == 1:
    st.warning("You have heart disease level 1! :worried:")
  elif prediction == 2:
    st.error("You have heart disease level 2! :sob:")
  elif prediction == 3:
    st.error("You have heart disease level 3! :sob:")
  elif prediction == 4:
    st.error("You have heart disease level 4! :sob:")
