"""The first step is to create an SMTP object, each object is used for connection
with one server."""

import smtplib


gmail_user = 'beehappytest1@gmail.com'
gmail_password = 'b33h@ppy'

sent_from = gmail_user
to = ['amyngph@gmail.com']
subject = "Happy"
body = "Hey, what's up?"


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

email_text = "asdf"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, email_text)
server.close()

#Next, log in to the server
#server.login("beehappy@gmail.com", "b33h@ppy")

#Send the mail
#msg = "Hello!" # The /n separates the message from the headers
#server.sendmail("h5861491@nwytg.net", "h5861491@nwytg.net", msg)
