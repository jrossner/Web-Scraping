import os
import smtplib
from scrapeHeadlines import check_headlines
from emailSender import send_email

username = os.environ.get('EMAIL_USERNAME')
passcode = os.environ.get('EMAIL_PASSCODE')
  
try:
  send_email(check_headlines("nfl",["buffalo","bill"]),username,passcode)
except Exception as ex:
  print(f'Could not execute due to: {ex}')
