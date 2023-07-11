#Import Streamlit library
import streamlit as st

import pandas as pd


# https://docs.google.com/spreadsheets/d/1W2smfo-KRBcU2DMM7tjwaW8BU5Ls2P7QvTmqoj_3slE/edit?usp=sharing
SHEET_ID = '1W2smfo-KRBcU2DMM7tjwaW8BU5Ls2P7QvTmqoj_3slE'
SHEET_NAME = 'Peringkat'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
print(df.head())

#MARKDOWN
#Displaying Markdown
st.markdown("# Beginner's Guide to Streamlit\n# with Python")
st.markdown('## Welcome to')
st.markdown("""### Streamlit's World""")

# LATEX
#Displaying Latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t}
= h^2 \left( \frac{\partial^2 u}{\partial x^2}
+ \frac{\partial^2 u}{\partial y^2}
+ \frac{\partial^2 u}{\partial z^2} \right)''')

# CODE
# Displaying Python Code
st.subheader("""Python Code""")
code = '''def hello():
print("Hello, Streamlit!")'''
st.code(code, language='python')
# Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
public static void main(String args[])
{
System.out.println("Hello World");
}
}""", language='javascript')
st.subheader("""JavaScript Code""")
st.code(""" <p id="demo"></p>
<script>
try {
adddlert("Welcome guest!");
}
catch(err) {
document.getElementById("demo").innerHTML = err.message;
}
</script> """)

# DATAFRAME
# Import Necessary libraries
import pandas as pd
import numpy as np
# defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
np.random.randn(20, 5),
columns=('col_no %d' % i for i in range(5)))
st.dataframe(df)


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


# METRICS
# Defining Metrics
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

#Defining Columns
c1, c2, c3 = st.columns(3)
# Defining Metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

# JSON
# Defining Nested JSON
st.json(
{ "Books" :
[{
"BookName" : "Python Testing with Selenium",
"BookID" : "1",
"Publisher" : "Apress",
"Year" : "2021",
"Edition" : "First",
"Language" : "Python",
},
{
"BookName": "Beginners Guide to Streamlit with Python",
"BookID" : "2",
"Publisher" : "Apress",
"Year" : "2022",
"Edition" : "First",
"Language" : "Python"
}]
}
)
