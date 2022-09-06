import os
import smtplib
from email.message import EmailMessage

def send_email(headlineBody,username,passcode):
  send_to = ['rosj016@gmail.com']
  sent_from = username
  message = EmailMessage()
  message['To'] = send_to
  message['Subject'] = 'ESPN Headlines For You'
  message['From'] = sent_from
  message.set_content(f'testing...: {headlineBody}')

  try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  except Exception as ex:
     print(f'Error 1: {ex}')
    
  try:
    smtp_server.ehlo()
  except Exception as ex:
    print(f'Error 2: {ex}')
 
  try:
    smtp_server.login(username,passcode)
  except Exception as ex:
    print(f'Error 3: {ex}')
    
  try:
    smtp_server.sendmail(sent_from, send_to[0], message)
  except Exception as ex:
    print(f'Error 4: {ex}')
 
  try:
    smtp_server.close()
    print("email sent!")
  except Exception as ex:
    print(f'Error 5: {ex}')
    
  #except Exception as ex:
      #print(f'Error: {ex}')
