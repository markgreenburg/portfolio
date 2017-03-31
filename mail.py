"""
Handles sending contact form emails
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

def send_email(name, email, message):
    """
    Sends email per config settings
    """
    # Set up some email content detials
    from_addr = config.FROM
    to_addr = config.TO
    sender_name_str = "Name: " + str(name) + "\n"
    sender_email_str = "Email: " + str(email) + "\n"
    message_str = "Message:\n" + str(message)
    contents = sender_name_str + sender_email_str + message_str

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = "New Contact Request"
    msg.attach(MIMEText(contents, 'plain'))

    server = smtplib.SMTP(config.SERVER, config.PORT)
    server.starttls()
    server.login(config.UID, config.PASSWORD)

    text = msg.as_string()
    server.sendmail(config.FROM, config.TO, text)
    server.quit()
    return
