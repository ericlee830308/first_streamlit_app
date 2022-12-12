import streamlit

streamlit.title('Hello World!')

streamlit.header('Hello World!')
streamlit.text('Hello World!1')
streamlit.text('Hello World!2')
streamlit.text('Hello World!3')
streamlit.text('Hello World!4')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(fruit_list.index))

streamlit.dataframe(fruit_list)
