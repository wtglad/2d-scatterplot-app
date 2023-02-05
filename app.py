import streamlit as st
import pandas as pd
from io import StringIO
import matplotlib.pyplot as plt

st.header('2D Scatterplot App w/ Point Highlighter')
uploaded_file = st.file_uploader("Upload a CSV")

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    variables = df.columns.tolist()
   
    x_input = st.selectbox(label='X value:', options=variables, index=1)
    y_input = st.selectbox(label='Y value:', options=variables, index=2)
    index_to_search = st.selectbox(label='Index', options=variables, index=0)

    if index_to_search is not None:
        search_value = st.selectbox(label='Value to highlight', options=df[index_to_search].tolist(), index=0)


    st.write('Plotting ' + str(y_input) + ' vs. ' + str(x_input))
    st.write('Highlighting value ' + str(search_value) + ' in index column ' + str(index_to_search))

    plt.figure(figsize=(10,10))
    plt.grid()
    plt.xlabel(str(x_input))
    plt.ylabel(str(y_input))
    plt.scatter(df[x_input], df[y_input])
    plt.scatter(df[df[index_to_search] == search_value][x_input], df[df[index_to_search] == search_value][y_input])
    st.pyplot(plt)