import streamlit as stream
import pandas

stream.set_page_config(layout="wide")

stream.title("Home", )
stream.title("")

col_one, col_two = stream.columns(2)

with col_one:
    stream.image("images/me.png", width=300)

with col_two:
    stream.title("Nate Weil")

    bio = """
    This is my bio. Yay!
    
    """
    stream.write(bio)

stream.info("Below you can find some of the apps that I have built.")

# Reads the csv data, indicating that the seperator is a semicolon.
data = pandas.read_csv("data.csv", sep=";")

# This chunk splits the app data evenly into two lists, alternating, for viewing in two columns.
list_one, list_two = [], []
for index, row in data.iterrows():
    if index % 2 == 0:
        list_one.append(row)
    else:
        list_two.append(row)


col_three, empty, col_four = stream.columns([1, 0.25, 1])

with col_three:
    for item in list_one:
        stream.subheader(item["Title"])

        if item["Image"] != "None":
            stream.image(f"images/{item['Image']}", width=150)
        else:
            stream.image("images/blank.png", width=150)

        stream.write(item["Description"])
        stream.write(f"[Source Code]({item['Link']})")

with col_four:
    for item in list_two:
        stream.subheader(item["Title"])

        if item["Image"] != "None":
            stream.image(f"images/{item['Image']}", width=150)
        else:
            stream.image("images/blank.png", width=150)

        stream.write(item["Description"])
        stream.write(f"[Source Code]({item['Link']})")