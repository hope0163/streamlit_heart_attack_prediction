import streamlit as st
import pandas as pd

def run_eda():
    df = pd.read_csv('data.csv')
    df.drop('Unnamed: 0', axis=1, inplace=True)
    st.dataframe(df)