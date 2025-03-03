import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Parent Dashboard of ABC School Management System")

Subjects = ['Eng', 'Math', 'SS', 'Science', 'Urdu']
Marks = [85, 75, 77, 69, 91]

plt.bar(Subjects,Marks )
plt.xlabel('Subjects')
plt.ylabel('Makrs')
plt.title('Cumulative results')

plt.savefig('Cumulative.jpg')
plt.show()
st.image('Cumulative.jpg')
chart_data = pd.DataFrame(Marks, Subjects)

st.bar_chart(chart_data)


