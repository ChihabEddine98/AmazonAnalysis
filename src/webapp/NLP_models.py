import os
import streamlit as st
import numpy as np
import pandas as pd

root_path = os.path.dirname(os.path.realpath(__file__))



st.write("Here's our first attempt at using data to create a table:")
st.latex(r'''
a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
\sum_{k=0}^{n-1} ar^k =
a \left(\frac{1-r^{n}}{1-r}\right)
''')

if st.checkbox('Show dataframe'):

    dataset_path = os.path.join(root_path, '..', 'common','reviews_dataset.csv')
    chart_data = pd.read_csv(dataset_path)

    chart_data