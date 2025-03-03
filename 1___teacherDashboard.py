import streamlit as st
import numpy as np

st.title("Teacher Dashboard of ABC School Management System")
st.title("Course Material Section")

uploaded_file = st.file_uploader("Upload Lecture material")
if uploaded_file is not None:
    st.download_button("Lecture material",uploaded_file)
st.page_link("https://www.w3schools.com/python/",label="Tutuorial", icon="🌎")

st.divider()
st.title("Video Lectures")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Lecture 1")
    video_file = open("PythonBasicsRevision.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
    l1f=st.feedback("stars")

with col2:
    st.header("Lecture 2")
    VIDEO_URL = "https://youtu.be/YBDr7qzvi4A"
    st.video(VIDEO_URL,autoplay=True)
    l2f= st.feedback("faces")

with col3:
    st.header("Lecture 3")
    VIDEO_URL = "https://youtu.be/tiwbbImZLYM?si=I_fQu9Cfan0TpBpl"
    st.video(VIDEO_URL,start_time=5)
    l3f=st.feedback("thumbs")

with st.container():
    st.write("This container lecture document and display current status of the course")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))


@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"


st.link_button("Exam","10___students_assessment.py")
