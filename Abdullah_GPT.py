import requests
import streamlit as st
from PIL import Image
import json
from gtts import gTTS
import speech_recognition as sr
import os
API_KEY = "AIzaSyD1bedJOi2IO0tnQBmi6oYNT8m_w4USI-Y"
API_URL ="https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
st.set_page_config(page_title="WELCOME TO THE AI DOCTOR👩🏻‍⚕️ GPT🤖", layout="centered")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
# ---------- Custom CSS ----------
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f9f9f9, #e3f2fd);
    }
    .title {
        font-size: 40px;
        color: #0d47a1;
        text-align: center;
        font-weight: bold;
    }
    .subtext {
        text-align: center;
        font-size: 18px;
        color: #444;
        margin-bottom: 30px;
    }
    .response-box {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        font-size: 17px;
        margin-top: 15px;
    }
    .stButton button {
        background-color: #0d47a1;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

        
st.markdown('<div class="title">WELCOME TO THE AI DOCTOR👩🏻‍⚕️ GPT🤖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtext">made by the 👑PRINCE👑 ABDULLAH MEMON😎</div>', unsafe_allow_html=True)

headers = {
    "Content-Type": "application/json",
}
params = {
    "key": API_KEY,
}
if True:
    input=st.text_input("FEEL TO FREE ASK QUESTION ABDULLAH GPT")
    button=st.button("ASK");
    
    if button: 
    # Check input in lowercased form
        st.success("You said: "+input)
        st.session_state.chat_history.append(("You ", input))
    
        if input=="":
            g=("Please write any thing you want to ask CHAT BOT GPT")
            
        elif input:   
             with st.spinner("plz wait we are processing and give you answer in few seconds🤗🤗🤗🤗🤗🤗"): 
                chat_payload = [
                    {"user :": speaker, "ai assestant :": message}
                    for speaker, message in st.session_state.chat_history
                    ]
                data = {
                    "contents": [
                        {
                            "parts": [
                                {"text":f"you are ai medical assitant you will give answers only medical type question and Give the answer in 2 languages: English and Urdu. Detect the user's language. If the user uses Urdu, then reply only in Urdu. If the user uses any other language (except Urdu), then reply only in English.and if some one ask you 'who made you' or 'who is you developer' or this type other questions you have to say 'ABDULLAH MEMON S/O ALI RAZA MADE ME AND HE TRAIN ME HE IS A SOFTWARE ENGINEER'.and check history{chat_payload} and current msg and then give correct answer,and plz don`t give thats type ans i.e 'Okay, I understand. I will only answer medical questions, and I will provide answers in both English and Urdu unless the user communicates solely in Urdu, in which case I will respond only in Urdu. I will also consider the conversation history to provide appropriate and accurate responses.Given the history ['user :': 'You ', 'ai assestant :': 'hi'] and your current message 'hi', this is a simple greeting and not a medical question. Therefore, I won't provide a medical answer.Since  this is a continuation of the initial exchange, I will respond in English.' just give answer of the user i.e(user='hi' )ans=(ai medical assistant ='Hi there! How can I help you with a medical question?'),dont give the answer of this msg just understant it='so i hope you understand very well and you will handle the user very well you will not disappointed the user'. so my question is ' {input} '"}
                                ]
                            }
                        ]
                    }
                response = requests.post(API_URL, headers=headers,params=params, json=data)
                #st.text(response.status_code)
                result = response.json()
                g=(result['candidates'][0]['content']['parts'][0]['text'])
               
        st.session_state.chat_history.append(("AI Doctor ", g))
        st.success("AI DOCTOR: "+g) 
    for speaker, message in st.session_state.chat_history:
        st.markdown(f"<div class='response-box'><b>{speaker}:</b> {message}</div>", unsafe_allow_html=True)    
