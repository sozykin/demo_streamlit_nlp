import streamlit as st
from transformers import pipeline

def create_model():
    model = pipeline("text-classification", model="SkolkovoInstitute/russian_toxicity_classifier")
    return model


model = create_model()
st.title('Определение токсичности текста')
text = st.text_input('Введите текст', 'Мамкин кубер-докер смузихлеб')
result = st.button('Определить токсичность')

if result:
    res = model(text)
    sent = res[0]['label']
    if sent == 'toxic':
        st.write('Текст токсичный')
    else:
        st.write('Текст нейтральный')
