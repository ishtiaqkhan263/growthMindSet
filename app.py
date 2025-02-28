import streamlit as st
import pandas as pd
import os
from io import BytesIO
# set up our app
st.set_page_config(page_title="Data Uploader", layout="wide")
st.title("Data Uploader")
st.write("Upload your data to the app and we'll process it for you.")
# upload file
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_file:
    for file in uploaded_file:
        file_exe = os.path.splitext(file.name)[-1].lower()

        if file_exe == ".csv":
            df = pd.read_csv(file)
        elif file_exe == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Invalid file type: {file_exe}")
            continue

        st.write(df)

        # display the information of the uploaded file 
        st.write(f"**File name**: {file.name}")
        st.write(f"**File size**: {file.size / 1024:.2f} KB")

        # display the first 5 rows of the dataframe
        st.write("preview the Head of the Dataframe")
        st.dataframe(df.head())

        # options for data cleaning and preprocessing
        st.subheader("Data Cleaning and Preprocessing")
        if st.checkbox(f"Clean Data {file.name}"):
            col1, col2 = st.columns(2)
        
            with col1:
                if st.button(f"Remove Duplicates {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates removed successfully!")

            with col2:
                if st.button(f"Fill Missing value {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing values filled successfully!")

        st.subheader("Select the columns to convert")
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns)



        my_dict = {
            'name'
        }

