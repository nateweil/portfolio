import streamlit as stream

stream.set_page_config(layout="wide")

stream.title("Home")
stream.title("")

col_one, col_two = stream.columns(2)

with col_one:
    stream.image("images/me.png", width=300)

with col_two:
    stream.subheader("Nate Weil")

    bio = """
    This is my bio. Yay!
    
    """
    stream.info(bio)