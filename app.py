import streamlit as st

from bbquote913.lib import get_quote

response = get_quote()  # assuming the function returns an author and a quote

st.write(response)
