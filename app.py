import streamlit as st
import pandas as pd
from list_offers import populate_with_dummy_data
st.title("Vacation offers")
st.text("This is a text box, I don't know what is doing!")

st.text_input("Enter the destination: ")

list_offers = []
populate_with_dummy_data(list_offers)
box = pd.DataFrame(list_offers)
st.dataframe(box)

# st.button(on_click = )