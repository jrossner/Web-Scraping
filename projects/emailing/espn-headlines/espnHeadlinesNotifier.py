import os
import smtplib
from scrapeHeadlines import check_headlines
from emailSender import send_email

try:
  send_email(check_headlines("nfl",["phi"]))
except:
  return "Issue encountered... could not execute"