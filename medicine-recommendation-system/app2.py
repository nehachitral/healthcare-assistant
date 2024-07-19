import streamlit as st
import datetime

# Set Streamlit theme and configuration with black background
st.set_page_config(
    page_title="Healthcare Reminders",
    page_icon=":alarm_clock:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customization for black background and improved layout
st.markdown(
    """
    <style>
    .main {
        background-color: #000000;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTimeInput input {
        background-color: #333333;
        color: white;
    }
    .stTitle {
        font-size: 3em;
        font-weight: bold;
    }
    .stSubheader {
        font-size: 1.5em;
        margin-top: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for reminders
if 'reminders' not in st.session_state:
    st.session_state['reminders'] = {
        'Monday': {'Morning': None, 'Afternoon': None, 'Evening': None, 'Night': None},
        'Tuesday': {'Morning': None, 'Afternoon': None, 'Evening': None, 'Night': None},
        'Wednesday': {'Morning': None, 'Afternoon': None, 'Evening': None, 'Night': None},
        'Thursday': {'Morning': None, 'Afternoon': None, 'Evening': None, 'Night': None},
        'Friday': {'Morning': None, 'Afternoon': None, 'Evening': None, 'Night': None},
        'Saturday': {'Morning': None, 'Afternoon': None, 'Evening': None, 'Night': None},
        'Sunday': {'Morning': None, 'Afternoon': None, 'Evening': None, 'Night': None},
    }

# Function to update reminders
def update_reminder(day, period, reminder_time):
    st.session_state['reminders'][day][period] = reminder_time

# Streamlit UI setup
def main():
    # Title and initial greeting
    st.title("Healthcare Reminders :pill:")
    st.write("Set reminders for taking medicine:")

    # Dropdown for selecting the day of the week
    day_of_week = st.selectbox("Select Day of the Week:", 
                               options=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # Reminder setting section for the selected day
    reminder_periods = ['Morning', 'Afternoon', 'Evening', 'Night']
    for period in reminder_periods:
        st.subheader(f"{day_of_week} {period} Reminder")
        reminder_time = st.time_input(f"Select {day_of_week} {period.lower()} time:", value=None, key=f"{day_of_week}_{period}_time")
        if st.button(f"Set {day_of_week} {period} Reminder", key=f"{day_of_week}_{period}_button"):
            update_reminder(day_of_week, period, reminder_time)
            if reminder_time:
                st.success(f"{day_of_week} {period} reminder set for {reminder_time.strftime('%I:%M %p')}!")
            else:
                st.error(f"{day_of_week} {period} reminder time not set!")

    # Display current reminders
    st.subheader("Current Reminders:")
    for day, periods in st.session_state['reminders'].items():
        st.write(f"**{day}:**")
        for period, time in periods.items():
            if time:
                st.write(f"- {period}: {time.strftime('%I:%M %p')}")
            else:
                st.write(f"- {period}: No reminder set")

if __name__ == "__main__":
    main()
