import pickle
import streamlit as st
 

st.title('Diabetes Diagnosis Assistant')

st.markdown('This application is meant to **_assist_ _doctors_ _in_ diagnosing**, if a patient has a **_Diabetes_ _or_ not** using few details about their health')

st.markdown('Please **Enter _the_ _below_ details** to know the results -')

# loading the trained model
pickle_in = open('DiabetesGB.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()

# defining the function which will make the prediction using the data which the user inputs 
def prediction(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):

    # Making predictions 
    prediction = classifier.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
     
    if prediction == 0:
        pred = 'are not a diabetic patient. Thank You!'
    else:
        pred = 'are a diabetic patient. Please see your doctor immediately!'
    return pred

    # this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Osadiapet Diabetes Prediction Machine Learning App</h1> 
    </div> 
    """
    

  
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 

    # following lines create boxes in which user can enter data required to make prediction 
    Pregnancies = st.number_input("Number of Times pregnant?")
    Glucose=st.number_input('Plasma Glucose Concentration (mg/dL) over 2 hours in an oral glucose tolerance test')
    BP=st.number_input('Diastolic Blood Pressure (mmHg)')
    ST=st.slider('Triceps skin fold thickness (mm)', 0.00, 120.00, 50.00)
    insulin=st.slider('Insulin level (2-Hour serum insulin (mu U/ml))', 0.00, 900.00, 10.00)
    BMI=st.slider('Body Mass Index (Weight in kg/height in m^2)', 0.00, 60.00, 1.00)
    dpf=st.slider('Diabetes pedigree Function (Likelihood of Diabetes based on Family History)', 0.000, 5.000, 0.649)
    Age=st.slider('Age (Years)', 0, 120, 50)
    
    result =""

     # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Pregnancies, Glucose, BP, ST, insulin, BMI, dpf, Age) 
        st.success('You {}'.format(result))
       
if __name__=='__main__': 
    main()
      

  