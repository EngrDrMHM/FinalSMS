# Create the table if it doesn't exist
import sqlite3
import streamlit as st
import pandas as pd
rowdata=[]
username=st.text_input("Enter user name")
username="Hussain"
def load_data():
    # Connect to the database
    conn = sqlite3.connect("../workouts.db")
    c = conn.cursor()

    # Create the table if it doesn't exist
    c.execute(
        f"CREATE TABLE IF NOT EXISTS workouts_{username} (id INTEGER PRIMARY KEY, activity TEXT, duration INTEGER, calories_burned INTEGER, avg_bpm INTEGER, date DATE DEFAULT 'N/A')")

    # Select the necessary columns for the current user
    c.execute(f"SELECT id, activity, duration, calories_burned, avg_bpm, date FROM workouts_{username}")
    rows = c.fetchall()

    # Close the connection
    conn.close()

    # Convert the data to a DataFrame
    df = pd.DataFrame(rows, columns=["id", "Activity", "Duration (min)", "Calories Burned", "Avg. BPM", "Date"])

    if df.empty:
        df = pd.DataFrame(columns=["id", "Activity", "Duration (min)", "Calories Burned", "Avg. BPM", "Date"])
        df = df.append(
            {"id": 1, "Activity": "Placeholder stats, remove after entering your data!", "Duration (min)": "0",
             "Calories Burned": "0", "Avg. BPM": "0", "Date": "N/A"}, ignore_index=True)

    return df

