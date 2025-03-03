import streamlit as st

with st.form("Test"):
    st.write("Question#01")
    answer1 = st.radio("Is python programming is case sensitive?",["Yes","No"],)
    st.write("Question#02")
    answer2 = st.radio("let v=50 the what is type of v", ["int", "String","Double","Float"],)
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        if answer1== "Yes":
            st.write(" answer1 Correct")
        else:
            st.write(" answer1 is Wrong")
        if answer2== "int":
            st.write("answer2 Correct")
        else:
            st.write(" answer2 is Wrong")