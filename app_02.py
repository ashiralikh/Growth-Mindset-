import streamlit as st

# Web app title
st.title("Growth Mindset Challenge")

st.write("""
         ### What is a Growth Mindset?
         A growth mindset is a mindset that focuses on continuous learning and growth,
         rather than fixed goals or limitations.
         """)

user_input = st.text_input("What is one way you practice a growth mindset?")

if user_input:
    st.write("Great! You shared this:", user_input)