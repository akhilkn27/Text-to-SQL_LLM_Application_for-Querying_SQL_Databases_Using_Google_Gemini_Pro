from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name Karnataka_District_Crop_Details and has the following columns - District_ID, District_Name, 
    Crop_Year,Crop_Name,Area_Cultivated,Production_Tons,Irrigation_Type \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) from Karnataka_District_Crop_Details;
    \nExample 2 - Tell me the total area cultivated across all districts?, 
    the SQL command will be something like this SELECT SUM(Area_Cultivated) as Total_Area_Cultivated 
    from Karnataka_District_Crop_Details;
    \nExample 3 - Tell me the average production in metric tons per district?, 
    the SQL command will be something like this SELECT AVG(Production_Tons) as Average_Production from 
    Karnataka_District_Crop_Details;
; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"Karnataka_District_Crop_Details.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)