import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "linetwangui04@gmail.com"
password = "xygyhivxitezzzps"

receiver = "linetwangui04@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
