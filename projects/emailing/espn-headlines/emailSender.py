import os
import smtplib
from email.message import EmailMessage

def send_email(headlineBody):
  username = os.environ.get('ESPN_EMAILER_USER')
  passcode = os.environ.get('ESPN_EMAILER_PASS')
  message = EmailMessage()
  
  message['To'] = 'rosj016@gmail.com'
  message['Subject'] = 'ESPN Headlines For You'
  message['From'] = username
  message.set_content(f'testing...: {headlineBody}')

  try:
      smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      smtp_server.ehlo()
      smtp_server.login(username,passcode)
      smtp_server.sendmail(sent_from, to, email_text)
      smtp_server.close()
      print("email sent!")
  except Exception as ex:
      print(f'Error: {ex}')
