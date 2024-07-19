import streamlit as st
import openai
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to interact with OpenAI's Chat API
def chat_with_openai(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the appropriate model
        messages=[
            {"role": "system", "content": "You are a healthcare assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
def main():
    st.set_page_config(
        page_title="Healthcare Assistant",
        page_icon=":hospital:",
        layout="wide",
        initial_sidebar_state="expanded",
        # CSS customization for background and text color
        style={"background-color": "#f0f0f0", "color": "#000000"}
    )

    st.title("Healthcare Assistant :pill:")
    st.write("Hello! I'm your healthcare assistant. How can I assist you today? :clipboard:")

    # User input text box
    user_input = st.text_input("You:", "")

    if st.button("Send"):
        if user_input:
            # Get response from OpenAI
            bot_reply = chat_with_openai(user_input)
            # Display bot's response
            st.text_area("Assistant:", value=bot_reply, height=150)

if __name__ == "__main__":
    main()
