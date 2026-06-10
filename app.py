import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Revisão Logística", layout="wide")

st.title("Revisão Executiva — Logística & Supply Chain")

with open("revisao.html", "r", encoding="utf-8") as f:
    html = f.read()

# Ajuste 'height' se o conteúdo aparecer cortado (ex.: 1200).
components.html(html, height=900, scrolling=True)
