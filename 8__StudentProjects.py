import streamlit as st

import pandas as pd

st.title(" List of Project By Student")

S1: bool=st.checkbox("Submitted",False,"s1")
S2: bool=st.checkbox("Submitted",False,"s2")
S3: bool=st.checkbox("Submitted",False,"s3")

df = pd.DataFrame(
    [
        {"Student": "Basheer", "Grade": "A", "is_Project_Submitted":S1 },
        {"Student": "Kareem", "Grade":"B" , "is_Project_Submitted":S2 },
        {"Student": "Noman", "Grade": "C", "is_Project_Submitted":S3 },
    ]
)
st.dataframe(df, use_container_width=False)


with st.form("Project Submission"):
    st.write("Provide Project Details")

    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")