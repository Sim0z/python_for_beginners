#!/usr/bin/path
import smtplib
import email.utils
from email.mime.text import MIMEText

ip = input("Target IP Address: ")
port = input("Target Port: ")
sender = ("test@domain.com")
receiver = ("test2@domain.com")
relay = MIMEText('Testing Open Relay')
relay['To'] = email.utils.formataddr(('RCPT TO:', receiver))
relay['From'] = email.utils.formataddr(('Mail From:', sender))

server = smtplib.SMTP(ip, port)
#Set Debug on
server.set_debuglevel(True)
try:
    server.sendmail(sender, [receiver], relay.as_string())
    print("Vulnerable to open relay")
except:
    print("Not Vulnerable to Open relay")
    server.quit()
