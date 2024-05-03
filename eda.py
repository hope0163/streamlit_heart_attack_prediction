import streamlit as st
import pandas as pd
from matplotlib import font_manager, rc

# 차트에 한글 나오게 설정
import platform
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

def run_eda():
    
    df = pd.read_csv('data.csv')
    df.drop('Unnamed: 0', axis=1, inplace=True)
    st.dataframe(df)