import streamlit as st
from ai21 import AI21Client


API_KEY = st.secrets['api-keys']['ai21-api-key']
client = AI21Client(api_key=API_KEY)
DEFAULT_MODEL = 'j2-ultra'

TOKENIZE_URL="https://api.ai21.com/studio/v1/tokenize"