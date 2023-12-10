import streamlit as st

import pandas as pd
import numpy as np

from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

st.set_page_config(page_title="NeuraNudge Solver", page_icon="📊")


openai_key = "enter key"

st.title("💻 Code Generator")


lang = st.sidebar.selectbox("🌐 Select Language", ("➕ C++", "☕ Java", "🐍 Python"))
lang = lang.split()[1]
print(lang)

custom_style = """
    <style>
        div[data-testid="stSidebar"][aria-expanded="true"] {
            background-color: black !important;
        }
    </style>
"""

st.markdown(custom_style, unsafe_allow_html=True)


# Settlement

import os

os.environ["OPENAI_API_KEY"] = openai_key

from langchain.llms import OpenAI

# LLM

llm = OpenAI(temperature=0.6)


from datetime import datetime


# Function to display a message
def display_message(author, content, timestamp):
    st.write("###")
    st.write(f"**{author}**: {content}")
    st.write(f"*Sent at {timestamp}*")
    st.markdown("---")


# Main Streamlit App
def main():
    # User input

    label = "Enter some query 👇"
    place_holder = "Message NeuraNudge Solver..."
    prompt_input = st.text_area(label, placeholder=place_holder, height=13)

    if prompt_input:
        
        current_time = datetime.now().strftime("%H:%M %p")

        display_message("User", prompt_input, current_time)

        # Simulate Assistant's reply
    
        prompt = "Write code in " + lang + " for problem " + prompt_input
        assistant_response = llm(prompt)

        print(assistant_response)

        current_time = datetime.now().strftime("%H:%M %p")
        
        custom_style = """
            <style>
                .highlight {
                    background-color: lightgray !important;
                    color: black !important;
                }
            </style>
        """

        # Display assistant's reply in a different style
        st.markdown(custom_style, unsafe_allow_html=True)
        
        formatted_response = assistant_response.replace('\t', '    ')

        
        st.code(f"**Assistant**: {formatted_response}")
        st.write(f"*Responded at {current_time}*")
        st.markdown("---")


# Run the app
if __name__ == "__main__":
    main()
