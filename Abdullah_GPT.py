import requests;
import streamlit as st;
import json

API_KEY = "AIzaSyAy8PSYddSJIQ0A7iaS0rxkwVv185z4UQI"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
st.title("WELCOME TO THE ABDULLAH GPT")
input=st.text_input("FEEL TO FREE ASK QUESTION ABDULLAH GPT")
button=st.button("ASK");
headers = {
    "Content-Type": "application/json",
}

params = {
    "key": API_KEY,
}

data = {
    "contents": [
        {
            "parts": [
                {"text":input}
            ]
        }
    ]
}
response = requests.post(API_URL, headers=headers, params=params, json=data)
if button:
    if response.status_code == 200:
        if input=="who make you" or input=="who is your owner" or input=="who made you" or input=="WHO MADE YOU" or input=="WHO IS YOUR OWNER" or input=="WHO MAKE YOU" or input=="tumah kis an banaya h" or input=="tumahe kis an banaya h" or input=="who created you" or input=="who design you" or input=="who give you knowledge":
            st.text("ABDULLAH MEMON S/O ALI RAZA IS THE MY OWNER and HE MADE ME");
        elif input=="":
            st.text("Please write any thing  you want to ask ABDULLAH GPT")
        else:    
            result = response.json()
            st.text(result['candidates'][0]['content']['parts'][0]['text'])
    else:
        print("Error:", response.status_code, response.text)
