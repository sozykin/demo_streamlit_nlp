import io
import streamlit as st
from transformers import pipeline

def create_generator():
    generator = pipeline('text-generation', model="sberbank-ai/mGPT" )
    return generator


generator = create_generator()
st.title('Уменьшенная копия системы Балабола от Яндекс')
text = st.text_input('Введите текст', 'Зашли как-то в Хабр программист на С++, инженер и разработчик веб-сайтов')
result = st.button('Продолжить текст')

if result:
    new_text = generator(text, max_length = 50)
    st.write(new_text[0]['generated_text'])
