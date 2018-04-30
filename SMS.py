import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("youremail@gmail.com", "yourpassword")
msg = "Message from the doorbell at home. Read email I have sent a photo!"
server.sendmail("youremail@gmail.com", "0404XXXXX8@transmitsms.com", msg)
#Your SMS provider. I use a company http://www.burstsms.com.au/. Burstsms uses the address @transmitsms.com
server.quit()
