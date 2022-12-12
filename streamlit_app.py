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
fruit_list = fruit_list.set_index('Fruit')

selected_fruits = streamlit.multiselect("Pick some fruits:", list(fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = fruit_list.loc[selected_fruits]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
