##Import Streamlit library
import streamlit as st
import time

seconds = 25

#MARKDOWN
#Displaying Markdown
st.markdown("# Latber 3 Barebow Semarang")
st.markdown('## Skor Perlombaan')

string1 = f'App ini akan update data secara otomatis setiap {seconds} detik. Jika anda ingin menstop fitur autoupdate, silakan klik "Stop" pada kanan atas. Jika anda ingin kembali mengaktifkan autoupdate, silakan klik tiga garis datar pada kanan atas, dan kemudian klik "Rerun"'
st.write(string1)


# DATAFRAME
# Import Necessary libraries
import pandas as pd
import numpy as np
 
# https://docs.google.com/spreadsheets/d/1W2smfo-KRBcU2DMM7tjwaW8BU5Ls2P7QvTmqoj_3slE/edit?usp=sharing
SHEET_ID = '1W2smfo-KRBcU2DMM7tjwaW8BU5Ls2P7QvTmqoj_3slE'
SHEET_NAME1 = 'PeringkatPI'
SHEET_NAME2 = 'PeringkatPA'
url1 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME1}'
url2 = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME2}'
colnames = ['Peringkat', 'Target', 'Nama', 'Klub','Total','S1-1','S1-2','S1-3','S1-4','S1-5','S1-6','Tot S1','S2-1','S2-2','S2-3','S2-4','S2-5','S2-6','Tot S2']

@st.cache(ttl=seconds)
def get_data(url):
    data = pd.read_csv(url, names = colnames)
    return data

st.markdown('###  Putri 30M')
data1 = get_data(url1)
placeholder1 = st.empty()
placeholder1.dataframe(data1)

st.markdown('###  Putra 30M')
data2 = get_data(url2)
placeholder2 = st.empty()
placeholder2.dataframe(data2)

time.sleep(seconds)
placeholder1.empty()
placeholder2.empty()

while True:
    data1 = get_data(url1)
    placeholder1.dataframe(data1)
    data2 = get_data(url2)
    placeholder2.dataframe(data2)
    time.sleep(seconds)
    placeholder1.empty()
    placeholder2.empty()
