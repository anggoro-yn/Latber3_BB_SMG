#Import Streamlit library
import streamlit as st

#MARKDOWN
#Displaying Markdown
st.markdown("# Latber 3 Barebow Semarang")
st.markdown('## Skor Perlombaan')

# DATAFRAME
# Import Necessary libraries
import pandas as pd
import numpy as np

# https://docs.google.com/spreadsheets/d/1W2smfo-KRBcU2DMM7tjwaW8BU5Ls2P7QvTmqoj_3slE/edit?usp=sharing
SHEET_ID = '1W2smfo-KRBcU2DMM7tjwaW8BU5Ls2P7QvTmqoj_3slE'
SHEET_NAME = 'PeringkatPI'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
print(df.head())
st.dataframe(df)
st.table(df)
