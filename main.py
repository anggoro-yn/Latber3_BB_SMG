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
SHEET_NAME = 'Peringkat'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
print(df.head())
st.dataframe(df)


# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(20, 5),
columns=('col_no %d' % i for i in range(5)))
# Highlighting minimum value objects
st.dataframe(df.style.highlight_max(axis=1,color='red').highlight_min(axis=1))

# TABLE
# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(20, 5),
columns=('col_no %d' % i for i in range(5)))
# defining data in table
st.table(df)
