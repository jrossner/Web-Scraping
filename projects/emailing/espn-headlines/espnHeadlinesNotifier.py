import os
import smtplib
from scrapeHeadlines import check_headlines
from emailSender import send_email

username = os.environ.get('ESPN_EMAILER_USER')
passcode = os.environ.get('ESPN_EMAILER_PASS')
  
try:
  hl = check_headlines("nfl",["buffalo","bill"])
  print(f'in eHN: {hl}')
  send_email(hl,username,passcode)
  print("Process executed.")
except Exception as ex:
  print(f'Issue encountered... could not execute due to: {ex}')
