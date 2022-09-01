import os
import smtplib

def send_email(headlineBody):
  username = os.environ.get('ESPN_EMAILER_USER')
  passcode = os.environ.get('ESPN_EMAILER_PASS')
  sent_from = username
  to = 'rosj016@gmail.com'
  subject = 'ESPN Headlines For You'
  body = f'testing...: {headlineBody}'

  email_text = """\
  From: %s
  To: %s
  Subject: %s


  %s
  """ % (sentFrom, ", ".join(to), subject, body)

  try:
      smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      smtp_server.ehlo()
      smtp_server.login(username,passcode)
      smtp_server.sendmail(sent_from, to, email_text)
      smtp_server.close()
      print("email sent!")
  except Exception as ex:
      return f'Error: {ex}'
