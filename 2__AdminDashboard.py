import streamlit as st
import pandas as pd
import openpyxl as xls

st.title("Admin Dashboard of ABC School Management System")
st.write(" Search for student by entering first Name")
choice=st.radio("Search Criteria",["In Current Class", " In All Students"])

python_Student=pd.read_excel('PythonAA.xlsx')
namesOfStudents=python_Student["Applicant_Name"].tolist()

StudentsNames = ['Kamran', 'basheer', 'Shabeer', 'Kiran',"Aisha Siddiqui"]
sname = st.text_input(key='sname',label='Type student name')
if choice=="In Current Class":
    if st.button('Check availability of student is school'):
        have_it = sname in StudentsNames
        'We have that student!' if have_it else 'We don\'t have that student in our school.'

        if 'clicked' not in st.session_state:
            st.session_state.clicked = False
else:

    if st.button('Check availability of student is school'):
        have_it = sname in namesOfStudents
        'We have that student!' if have_it else 'We don\'t have that student in our school.'

        if 'clicked' not in st.session_state:
            st.session_state.clicked = False


FeePaidforStudentsNames = [{'Kamran':False, 'basheer':False, 'Shabeer':False, 'Kiran':False}]
snameforFee = st.text_input(key='snameforFee',label='Type student name')

if st.button('pay Fee for student','listStudentSearch'):
    have_it = snameforFee in StudentsNames
    'We have paid fee for student! ' if have_it else 'We don\'t have that student in our school.'

st.divider()
pstname=python_Student['Applicant_Name']

snameforPython = st.text_input(key='psname',label='Type student name')

if st.button('Check availability of student is school python','PythonStudentSearching'):
    have_it = snameforPython in namesOfStudents
    'We have that student!' if have_it else 'We don\'t have that student in our school.'

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False


FeePaidforStudentsNames = [{'Kamran':False, 'basheer':False, 'Shabeer':False, 'Kiran':False}]
psnameforFee = st.text_input(key='psnameforFee',label='Type student name')

if st.button('pay Fee for student','pthonStudentFee'):
    have_it = psnameforFee.lower() in StudentsNames
    'We have paid fee for student! ' if have_it else 'We don\'t have that student in our school.'
    FeePaidforStudentsNames[{pstname}]=have_it


st.write(python_Student)
