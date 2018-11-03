"""The first step is to create an SMTP object, each object is used for connection
with one server."""

#TODO: Add key for email/password so it's not online

import smtplib

def sendEmailTo(to):
    """
    to should be a list of emails to send to
    """
    gmail_user = 'beehappytest1@gmail.com'
    gmail_password = 'b33h@ppy'

    sent_from = gmail_user
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

if __name__ == "__main__":
    sendEmailTo('amyngph@gmail.com')
