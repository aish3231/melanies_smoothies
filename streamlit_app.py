# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app

st.title("My Parents New Healthy Diner")
st.write( 
    """Breakfast Menu
    Omega 3 and Blueberry Oatmeal
    """)

cnx = st.connection("snowflake")
session = cnx.session()
