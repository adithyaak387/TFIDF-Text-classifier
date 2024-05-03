import streamlit as st 
import joblib
model=joblib.load("news-classification-model.pkl")
#define sentimental labels
news_labels={'0':'Technical','1':'Business','2':'Sports','3':'Entertainment','4':'Politics'}
#create streamlit app
st.title("News Classification")
#input text are
user_input=st.text_area("Enter news here:")
#prediction button
if st.button("Predict"):
    predicted_label=model.predict([user_input])[0]
    predicted_news_label=news_labels[str(predicted_label)]
    #display predicted sentiment
    st.info(f"Predicted sentiment: {predicted_news_label}")
    