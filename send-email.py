import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()

server.login("from email address","email password")
server.sendmail("from email address","to email address","Your Message")
server.sendmail("from email address","to email address","Your Message")
server.sendmail("from email address","to email address","Your Message")
server.close()