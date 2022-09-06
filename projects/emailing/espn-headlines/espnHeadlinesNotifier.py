import os
import smtplib
from scrapeHeadlines import check_headlines
from emailSender import send_email

username = os.environ.get('ESPN_EMAILER_USER')
passcode = os.environ.get('ESPN_EMAILER_PASS')
  
try:
  send_email(check_headlines("nfl",["buffalo","bill"]),username,passcode)
except Exception as ex:
  print(f'Could not execute due to: {ex}')
