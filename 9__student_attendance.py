import streamlit as st
from datetime import time
st.title("ATTENDANCE SHEET")
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import datetime

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d




data_df = pd.DataFrame(
    {
        "Class day": [
            date(2025, 1, 1),
            date(2025, 5, 3),
            date(2025, 5, 19),
            date(2025, 8, 17),
        ]
    }
)

st.data_editor(
    data_df,
    column_config={
        "birthday": st.column_config.DateColumn(
            "Birthday",
            min_value=date(1900, 1, 1),
            max_value=date(2005, 1, 1),
            format="DD.MM.YYYY",
            step=1,
        ),
    },
    hide_index=True,
)


data_df = pd.DataFrame(
    {
        "Class Slot": [
            time(12, 30),
            time(18, 0),
            time(9, 10),
            time(16, 25),
        ]
    }
)


st.data_editor(
    data_df,
    column_config={
        "Class_Slot": st.column_config.TimeColumn(
            "Class_Slot",
            min_value=time(8, 0, 0),
            max_value=time(19, 0, 0),
            format="hh:mm a",
            step=60,
        ),
    },
    hide_index=True,
)





data = {"applicantName": ["Abdul Ahad Shaikh", "Abdul Basit Memon", "Abdul Hafeez Bhayo"], "FatheName": ["Abdul Aziz Memon", "kSAREEM", "Abdul Wahab Bhayo"] , "Monday":[False,False,False],"Tuesday":[False,False,False],"Wednesday":[False,False,False],"Thursday":[False,False,False],"Friday":[False,False,False]}


roster=pd.read_excel("PITP.xlsx")

df = pd.DataFrame(data)
#st.dataframe(df)
st.data_editor(
    roster,
    column_config={
        "Monday": st.column_config.CheckboxColumn(
            "Monday",
            help="Attendance",
            default=False,
        ),
"Tuesday": st.column_config.CheckboxColumn(
            "Tuesday",
            help="Attendance",
            default=False,
        )
    },
    disabled=["widgets"],
    hide_index=True,
)