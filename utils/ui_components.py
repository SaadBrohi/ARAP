# utils/ui_components.py

import streamlit as st

def render_chat_bubble(role, message):
    if role == "user":
        color = "#2C3E50"
        label = "🧑‍💻 You"
    else:
        color = "#145A32"
        label = "🤖 QueryVerse"

    st.markdown(
        f"""
        <div style='background-color:{color};padding:15px;border-radius:10px;margin-bottom:10px;color:white'>
        <b>{label}</b><br>{message}
        </div>
        """,
        unsafe_allow_html=True
    )

def loading_animation(message="Working..."):
    st.markdown(
        f"""
        <div style="font-size:16px; padding:10px; color:gray;">
            ⏳ {message}
        </div>
        """, 
        unsafe_allow_html=True
    )
