import streamlit as stream
from send_email import send_email

stream.header("Send A Message")

with stream.form(key="form"):
    address = stream.text_input("Email address")
    message = stream.text_area("Message")

    button = stream.form_submit_button("Send")
    if button:
        send_email(address, "Contact Form Submission", message)
        stream.info("Message successfully sent!")