import os
import smtplib
from scrapeHeadlines import check_headlines
from emailSender import send_email

try:
  hl = check_headlines("nfl",["buffalo","bill"])
  print(f'in eHN: {hl}')
  send_email(hl)
  print("Process executed.")
except Exception as ex:
  print(f'Issue encountered... could not execute due to: {ex}')
