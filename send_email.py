import smtplib, ssl

# Send an email from yourself to yourself, with the submitter's information attached. I guess not an easy way to allow
# emails from random people?
def send_email(email_address, subject, body):
    host = "smtp.gmail.com"
    port = 465

    username = "nateweil1993@gmail.com"
    password = "xifptdxsivxxflzq"

    receiver = "nateweil1993@gmail.com"
    context = ssl.create_default_context()

    message = f"Subject: {subject}\n{body}\n\n\nSender's email: {email_address}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)