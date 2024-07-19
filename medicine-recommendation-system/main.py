import streamlit as st
import time

# Set Streamlit theme and configuration with black background
st.set_page_config(
    page_title="Healthcare Assistant",
    page_icon=":hospital:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar navigation options and corresponding Python files
page_options = {
    "Home": "home.py",
    "Medicine Recommendation": "app.py",
    "Label Reader/Prescription": "app1.py",
    "Reminders": "app2.py"
}

# Title and initial greeting
st.title("Healthcare Assistant :pill:")
st.write("Hello! I'm your healthcare assistant. How can I assist you today? :clipboard:")

# Sidebar selection for navigation
selection = st.sidebar.selectbox("Go to", list(page_options.keys()))

# Conditionally load the selected page
if selection == "Home":
    # Display content related to healthcare
    st.header("Healthcare Information :hospital:")
    st.markdown("""
    Here you can find information related to healthcare topics.
    Include any relevant content or resources you want to display.
    """)

    # Search engine placeholder
    st.header("Search Engine :mag_right:")
    user_query = st.text_input("Ask me anything about healthcare")

    if user_query:
        st.write("You asked:", user_query)
        # Wait for 10 seconds
        time.sleep(10)
        # Display Paracetamol information
        st.write("""
        Paracetamol is a medicine used to treat mild to moderate pain. Paracetamol can also be used to treat fever (high temperature). 
        It's dangerous to take more than the recommended dose of paracetamol. Paracetamol overdose can damage your liver and cause death.
        """)

elif selection in page_options:
    # Load the selected Python file when its name is selected from the sidebar
    selected_file = page_options[selection]
    try:
        st.write(f"Loading {selected_file}...")
        exec(open(selected_file).read())  # Execute the selected file's contents
    except FileNotFoundError:
        st.error(f"Error: {selected_file} not found.")
