from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def checklUpcomingEarnings():
  link = "https://www.marketbeat.com/stocks/NYSE/APLE/earnings/"
  page_request = requests.get(link)
  soup = BeautifulSoup(page_request.text,"lxml")
  head = str(soup.find("dd", class_ = "stat-summary-heading my-1"))
  
  earningsDate = head.split('my-1">')[1].split('<span')[0]
  
  if (datetime.today()+timedelta(days=7)).strftime('%b. %-d') == earningsDate:
    # earnings date is 1 week from today
    text = f'Apple REIT announces earnings 1 week from today ({earningsDate}).\n'
  else:
    text = False
  
  
  if lastDayToOwn == (today+timedelta(days=1)).strftime('%Y-%m-%d'):
    text = "Tomorrow is Apple REIT's Ex-Dividend Date.\n\nWhoever owns APLE stock at the end of today will receive the next dividend."
  elif lastDayToOwn == (today+timedelta(days=7)).strftime('%Y-%m-%d'):
    text = f"Apple REIT's Ex-Dividend Date is 1 Week from today. \n\nWhoever owns APLE stock by the end of {(today+timedelta(days=6)).strftime('%A %B %d')} will receive the next dividend."
  else:
    text = False

  return text

