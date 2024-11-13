import os
from dotenv import load_dotenv
load_dotenv()

test = os.getenv('MY_SECRET')
print(test)

from openai import OpenAI
import streamlit as st

st.title('title')
st.header('header')
st.subheader('subheader text')
st.text('normal text')

