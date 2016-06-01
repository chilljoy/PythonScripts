import smtplib

fromaddr = 'kris.monier@mutualmobile.com'
toaddrs  = 'kris.monier@mutualmobile.com'
msg = 'Why,Oh why!'
username = 'kris.monier@mutualmobile.com'
password = 'vvvdmdqtxhhmpjwe'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()