##Import Streamlit library
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
colnames = ['Peringkat', 'Target'. 'Nama', 'Klub','Total','S1-1','S1-2','S1-3','S1-4','S1-5','S1-6','Tot S1','S2-1','S2-2','S2-3','S2-4','S2-5','S2-6','Tot S2']
df = pd.read_csv(url, names = colnames)
#print(df.head())
st.dataframe(df)
#st.table(df)
