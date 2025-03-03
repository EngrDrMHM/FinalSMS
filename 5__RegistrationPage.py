import datetime

import pandas as pd
import streamlit as st

st.write("Welcome to ABC School")
st.title(" This Registration page title")
st.write("## Submit Your Biodata using this page")
st.subheader(" Personal Information collection section")
st.divider()
name = st.text_input("Name", "Enter your name Here")
fname = st.text_input("Father Name", "Enter your Father name Here")
Age = st.text_input("Age", "Enter your name Here")
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)
if picture:
    st.image(picture)
uploaded_file = st.file_uploader("Choose a profile picture file")
if uploaded_file is not None:
    st.image(uploaded_file)
# upload profile picture

Adrress = st.text_input("Address", "Enter your Addrees")
List_of_Cities = pd.DataFrame(
    {
        "Cities": [
            "Larkana ",
            "Sukkur",
            "Khairpur",
            "Naushahro Feroze",
            "Mehrabpur",
            "Kandiaro",
            "Rohri"
        ],
    }
)

citySelected = st.data_editor(
    List_of_Cities,
    column_config={
        "Cities": st.column_config.SelectboxColumn(
            "Select Your City",
            help="This option is to add your city to describe your address",
            width="medium",
            options=[
                "Larkana ",
                "Sukkur",
                "Khairpur",
                "Naushahro Feroze",
                "Mehrabpur",
                "Kandiaro",
                "Rohri",
            ],
            required=True,
        )
    },
    hide_index=True,
)
st.write(" You gave selected City", citySelected)
st.divider()

st.write("Select Date Of Birth")
dob = st.date_input("What is your birthday", datetime.date(1984, 7, 6))
st.write("Your birthday is:", dob)

ClassTimeSlot = st.time_input("Class Time Slot", datetime.time(9, 15))
st.write("Class Time Slot", ClassTimeSlot)

st.divider()
DescribeYourSelf = st.text_input("DescribeYourSelf", "Enter Describion sbout YourSelf Here")
nextkin = st.text_input("NextKin", "Enter Next Kin")
gender = st.radio("Gender", ["Male", "Female", "Other"])
st.divider()
st.subheader(" Hobbies")
TV = st.checkbox("Watching TV ")
Cricket = st.checkbox('Cricket')
ReadBooks = st.checkbox('ReadBooks')
st.subheader(" Feedback")
yourFeedback = st.feedback("stars")
options = ["North", "East", "South", "West", "Center"]
selection = st.pills("Directions", options, selection_mode="single")

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

st.link_button("Go to gallery", "https://streamlit.io/gallery")

on = st.toggle("Show picture")

if on:
    st.image("fpsLogo.png")

if st.button("Submit"):
    file = open('DataRegistration.txt', 'w')
    file.write(
        f"Your Name is `{name}` and your father name is `{fname}` and your age is`{Age} and your address is :'{Adrress}' and you are living in city:'{citySelected}'")
    file.write(f"your date of brith is '{dob}' Gender: '{gender}' your feedback on app'{yourFeedback}'")
    file.close()

    st.write(f"Your data has been saved")
