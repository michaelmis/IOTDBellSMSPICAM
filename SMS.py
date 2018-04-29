import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("youremail@gmail.com", "yourpassword")
msg = "Message from the doorbell at home. Read email I have sent a photo!"
server.sendmail("youremail@gmail.com", "0404XXXXX5@transmitsms.com", msg)
#Burstsms uses the address @transmitsms.com for communication to the "email to SMS" service.
server.quit()
