import pandas as pd
import numpy as np
import pickle 
import streamlit as st

st.title('Predicting Diabetes With Machine Learning techniques')
st.header('Input the required parameter')

model1=pickle.load(open('GradientBoosting.pkl','rb'))

def predict(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    input=np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,
        Age]]).astype(np.float64)
    Prediction=model1.predict(input)
    return(float(Prediction))

def main():
    
    
    html_temp = """
        <div style="background-color:#ff9966;padding:5px;margin-bottom:20px"> </div>
        """
    
main()
pregnancy=st.text_input('How many times have you been pregnant?')
Glucose=st.text_input('What is your glucose level?')
BP=st.text_input('What is your Blood Pressure level? ')
SkinThickness=st.text_input('What is the thickness of your skin?')
Insulin=st.text_input('What is your insulin level?')
BMI=st.text_input('What is your BMI')
DiabetesPedigreeFunction=st.text_input('what is your DiabetesPedigreeFunction')
Age=st.text_input('What is your age')

if st.button('predict'):
    output=predict(pregnancy, Glucose, BP, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
    
    if output==1.0:
        st.success(' You are a potential Diabetic patient, Take care!')
    else:
        st.success(" That's cool, you are not a diabetic patient")

