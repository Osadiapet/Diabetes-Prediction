import pickle
import streamlit as st
 
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
        pred = 'a diabetic patient. Please see your doctor!'
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
    Pregnancies = st.number_input("How many times have you been pregnant?")
    Glucose=st.slider('Glucose level', 0, 120, 50)
    BP=st.slider('Blood Pressure level', 0, 120, 50)
    ST=st.slider('Skin Thickness', 0, 120, 50)
    insulin=st.slider('Insulin level', 0, 1000, 250)
    BMI=st.slider('BMI', 0, 120, 50)
    dpf=st.slider('Diabetes pedigree Function', 0.00, 2.50, 0.50)
    Age=st.slider('Age', 18, 100, 50)
    
    result =""

     # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(Pregnancies, Glucose, BP, ST, insulin, BMI, dpf, Age) 
        st.success('You {}'.format(result))
       
if __name__=='__main__': 
    main()
      

  