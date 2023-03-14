import streamlit as st
import numpy as np

# Set page title
st.set_page_config(page_title="Family 1000 BIRM")

# Add a title to the app
st.title("Kuis Family 1000 BIRM")

# Add a text input widget
text_input = st.text_input("Masukkan Jawabannya")

# Add a submit button
if st.button("Check Survey"):
    # Generate a random score between 0-100
    score = int(np.random.uniform(0, 101))
    # Display the score to the user
    st.write(f"Hasil Survey Untuk '{text_input}' adalah {score}")

if st.button("Clear"):
    # Clear the text input
    text_input = ""
    # Clear the score display
    score = None
