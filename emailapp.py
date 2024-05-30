import streamlit as st
import pickle
import pandas as pd
from io import StringIO

#loaded model from the classification notebook
model = pickle.load(open('email_classification_model.pkl', 'rb'))
vectorizer = pickle.load(open('email_vectorizer.pkl', 'rb'))

#Streamlit ui for email classification model

st.set_page_config(
    page_icon='📧',
    page_title="Email Classification",

) 
st.header("E-mail Detection App :email:")
st.subheader('Type an Email in the text area below and we can check if it is a Phishing attempt or if its and legitimate email.')
email = st.text_area('type in here the email you would like to check')
submit_button = st.button(label='Check')
if submit_button:
    if email:
        prediction = model.predict(vectorizer.transform([email]))
        if prediction[0] == 1:
            st.write("This email is classified as safe and not spam.")
        else:
            st.write("This email is classified as spam.")
    else:
        st.write("Please enter an email to check.")
    #st.success('this email is: {}'.format())
        

st.subheader('You can also upload a txt file that contains the contents of your txt file to also see if your file was spam or not')
upload = st.file_uploader('please upload a file')
if upload is not None:
    # To read file as bytes:
    bytes_data = upload.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(upload.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

button = st.button('Check file for spam')
if button:
    if upload:
        prediction = model.predict(vectorizer.transform([upload]))
        if prediction[0] == 1:
            st.write("This email is classified as safe and not spam.")
        else:
            st.write("This email is classified as spam.")
    else:
        st.write("Please enter an email to check.")
    
